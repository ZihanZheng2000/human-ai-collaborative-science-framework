"""Agent adapters.

Every agent is configured in workflow.config.json and reached through one of
these adapters:

- cli: any command-line agent (Claude Code, Codex, Gemini CLI, Aider, ...).
  Works in the repository and can edit files and run code.
- anthropic: Claude through the official Anthropic Python SDK. Read-only:
  the orchestrator sends file contents and writes the reply to disk.
- openai_compatible: any endpoint that speaks the OpenAI chat-completions API
  (OpenAI, and many hosted or local model servers). Read-only, like anthropic.
- human: a person performs the role; the task is written to the inbox.
"""

import json
import os
import shlex
import subprocess
from dataclasses import dataclass
from pathlib import Path


class AgentError(Exception):
    pass


@dataclass
class AgentResult:
    text: str
    returncode: int = 0
    session_id: str = None


class CliAdapter:
    kind = "cli"

    def __init__(self, name: str, spec: dict):
        self.name = name
        self.spec = spec

    def command_for(self, role: str) -> list:
        return self.spec.get("role_commands", {}).get(role) or self.spec["command"]

    def run_task(self, prompt: str, role: str, cwd: Path, log_path: Path,
                 session_id: str = None, framework_dir: Path = None) -> AgentResult:
        """Run one agent session with `cwd` (the project folder) as working directory.

        Placeholders in the command: {prompt}, {prompt_file}, {project_dir},
        {framework_dir}. With a "session" spec (researcher only), the session id
        is read from the agent's JSON output and the next call in the same stage
        resumes it.
        """
        template = list(self.command_for(role))
        session_spec = self.spec.get("session") if role == "researcher" else None
        if session_spec:
            template += session_spec.get("start_args", [])
            if session_id:
                template += [a.replace("{session_id}", session_id) for a in session_spec.get("resume_args", [])]
        prompt_file = log_path.with_suffix(".prompt.md")
        prompt_file.parent.mkdir(parents=True, exist_ok=True)
        prompt_file.write_text(prompt, encoding="utf-8")
        subs = {"{prompt_file}": str(prompt_file), "{project_dir}": str(cwd),
                "{framework_dir}": str(framework_dir or cwd)}
        argv = []
        for part in template:
            for key, val in subs.items():
                part = part.replace(key, val)
            argv.append(part.replace("{prompt}", prompt))
        stdin = prompt if self.spec.get("stdin") else None
        env = {**os.environ, **self.spec.get("env", {})}
        try:
            proc = subprocess.run(
                argv,
                cwd=cwd,
                input=stdin,
                capture_output=True,
                text=True,
                timeout=self.spec.get("timeout_seconds", 3600),
                env=env,
            )
        except FileNotFoundError as exc:
            raise AgentError(f"agent '{self.name}': command not found: {argv[0]}") from exc
        except subprocess.TimeoutExpired as exc:
            raise AgentError(f"agent '{self.name}': timed out after {exc.timeout}s") from exc
        shown = [a if a != prompt else "<prompt>" for a in argv]
        log_path.write_text(
            f"$ {shlex.join(shown)}\n(prompt in {prompt_file.name})\n"
            f"returncode: {proc.returncode}\n\n--- stdout ---\n{proc.stdout}\n--- stderr ---\n{proc.stderr}\n",
            encoding="utf-8",
        )
        text, sid = proc.stdout, None
        if session_spec:
            try:
                data = json.loads(proc.stdout.strip().splitlines()[-1])
                sid = data.get(session_spec.get("id_key", "session_id"))
                text = data.get(session_spec.get("text_key", "result"), proc.stdout)
            except (ValueError, IndexError, AttributeError):
                pass  # no JSON: run continues without session continuity
        return AgentResult(text, proc.returncode, sid)


class AnthropicAdapter:
    """Claude via the official Anthropic SDK (pip install anthropic)."""

    kind = "anthropic"

    def __init__(self, name: str, spec: dict, client=None):
        self.name = name
        self.spec = spec
        self._client = client

    def client(self):
        if self._client is None:
            try:
                import anthropic
            except ImportError as exc:
                raise AgentError("agent '%s' needs the Anthropic SDK: pip install anthropic" % self.name) from exc
            # Credentials resolve from the environment (ANTHROPIC_API_KEY, an
            # `ant auth login` profile, ...); api_key_env selects another variable.
            key_env = self.spec.get("api_key_env")
            kwargs = {"api_key": os.environ[key_env]} if key_env and key_env in os.environ else {}
            self._client = anthropic.Anthropic(**kwargs)
        return self._client

    def complete(self, system: str, user: str) -> str:
        params = dict(
            model=self.spec["model"],
            max_tokens=self.spec.get("max_tokens", 64000),
            system=system,
            messages=[{"role": "user", "content": user}],
            thinking={"type": "adaptive"},
            output_config={"effort": self.spec.get("effort", "high")},
        )
        if self.spec.get("fallbacks", True):
            # Re-run a safety-classifier decline on Anthropic's recommended fallback model.
            params["betas"] = ["server-side-fallback-2026-07-01"]
            params["fallbacks"] = "default"
        with self.client().beta.messages.stream(**params) as stream:
            message = stream.get_final_message()
        if message.stop_reason == "refusal":
            detail = getattr(message, "stop_details", None)
            raise AgentError(f"agent '{self.name}' declined the request: {detail}")
        text = "".join(block.text for block in message.content if block.type == "text")
        if message.stop_reason == "max_tokens":
            raise AgentError(f"agent '{self.name}' hit max_tokens; raise max_tokens in the config")
        return text


class OpenAICompatibleAdapter:
    """Any OpenAI chat-completions endpoint (pip install openai)."""

    kind = "openai_compatible"

    def __init__(self, name: str, spec: dict, client=None):
        self.name = name
        self.spec = spec
        self._client = client

    def client(self):
        if self._client is None:
            try:
                import openai
            except ImportError as exc:
                raise AgentError("agent '%s' needs the OpenAI SDK: pip install openai" % self.name) from exc
            key_env = self.spec.get("api_key_env", "OPENAI_API_KEY")
            self._client = openai.OpenAI(
                api_key=os.environ.get(key_env), base_url=self.spec.get("base_url")
            )
        return self._client

    def complete(self, system: str, user: str) -> str:
        resp = self.client().chat.completions.create(
            model=self.spec["model"],
            messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
            **self.spec.get("extra_params", {}),
        )
        choice = resp.choices[0]
        if choice.finish_reason == "length":
            raise AgentError(f"agent '{self.name}' hit its output limit")
        return choice.message.content or ""


class HumanAdapter:
    """A person performs the role. The engine writes the task to the inbox."""

    kind = "human"

    def __init__(self, name: str, spec: dict):
        self.name = name
        self.spec = spec


def make_adapter(name: str, spec: dict):
    kind = spec["kind"]
    if kind == "cli":
        return CliAdapter(name, spec)
    if kind == "anthropic":
        return AnthropicAdapter(name, spec)
    if kind == "openai_compatible":
        return OpenAICompatibleAdapter(name, spec)
    if kind == "human":
        return HumanAdapter(name, spec)
    raise AgentError(f"unknown agent kind: {kind}")
