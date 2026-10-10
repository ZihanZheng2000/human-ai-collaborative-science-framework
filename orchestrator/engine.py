"""The workflow state machine.

Per stage: work -> review -> triage -> gate. The engine stops only at human
nodes (inbox items): Pre-Planning setup, Tier 1 checkpoints raised by the
researcher, Tier 2 gates, tasks assigned to a human agent, and stuck states.
"""

import json
import re
import shutil
import tempfile
from datetime import date
from pathlib import Path

from . import STAGES, decision_log, inbox, prompts
from .adapters import AgentError, make_adapter
from .config import review_mode_for, reviewer_for

WAITING = "waiting"
DONE = "done"
RUNNING = "running"

TEXT_SUFFIXES = {".md", ".txt", ".csv", ".json", ".py", ".r", ".R", ".tex", ".yaml", ".yml", ".toml", ".ipynb", ".tsv"}


class Engine:
    def __init__(self, repo_root: Path, config: dict, project_dir: Path,
                 interactive: bool = True, input_fn=input, print_fn=print, adapters=None):
        self.root = repo_root.resolve()
        self.cfg = config
        self.project = project_dir.resolve()
        self.rel_project = str(self.project.relative_to(self.root))
        self.interactive = interactive
        self.input_fn = input_fn
        self.print = print_fn
        self._adapters = adapters or {}
        self.state_path = self.project / ".workflow" / "state.json"
        self.state = json.loads(self.state_path.read_text()) if self.state_path.exists() else None

    # ------------------------------------------------------------------ setup

    def init_project(self, topic: str, run_id: str = None, use_config_defaults: bool = False) -> None:
        p = self.project
        for sub in ["packages", "deliverables", "notes", "archive", "inbox/pending", "inbox/answered",
                    "artifacts/input/domain-materials", "artifacts/data", "artifacts/code",
                    "artifacts/logs", "artifacts/tables", "artifacts/figures", "artifacts/validation",
                    ".workflow"]:
            (p / sub).mkdir(parents=True, exist_ok=True)
        slug = p.name
        run_id = run_id or f"{slug}-run1"
        (p / "artifacts" / run_id / "agent").mkdir(parents=True, exist_ok=True)
        decision_log.ensure(p / "decision-log.md", self.root / "templates/decision-log.md", slug)
        if not (p / "run-notes.md").exists():
            shutil.copy(self.root / "templates/example-run-notes.md", p / "run-notes.md")
        if not (p / "README.md").exists():
            (p / "README.md").write_text(
                f"# {slug}\n\n## Status\n\n- current stage: Pre-Planning setup\n- active package: none\n"
                "- last decision: none\n- open escalations: none\n- deferred items due soon: none\n"
                "- current workflow mode and reviewer strategy: (set at setup)\n"
                "- next action: answer the setup questions\n- user decision needed now: setup\n\n"
                f"## User request\n\n{topic}\n\n## Research question\n\n(to be set in Planning)\n", encoding="utf-8")
        wf = self.cfg.get("workflow", {})
        self.state = {
            "project": slug, "run_id": run_id, "topic": topic, "stage": "planning", "step": "setup",
            "revision": 1, "attempts": 0, "notes": [], "human_tasks_done": [],
            "settings": {"mode": wf.get("mode", "step-by-step"), "reviewer": wf.get("reviewer", "use"),
                         "gates": wf.get("gates", "real")},
            "history": [],
        }
        synthetic = self.state["settings"]["gates"] == "synthetic"
        if use_config_defaults or synthetic:
            self._log("Pre-Planning", "tier-1 checkpoint",
                      f"Setup from workflow.config.json: mode={self.state['settings']['mode']}, "
                      f"reviewer={self.state['settings']['reviewer']}, gates={self.state['settings']['gates']}",
                      "orchestrator", "workflow.config.json",
                      "synthetic" if synthetic else "user (config file)",
                      "synthetic" if synthetic else "nominal: setup taken from the config file, not presented")
            self.state["step"] = "work"
        else:
            self._write_setup_questions()
        self._save()

    def _write_setup_questions(self) -> None:
        roles = self.cfg["roles"]
        questions = {
            "SETUP-mode": ("workflow mode", [
                "step-by-step (recommended for real research): each Tier 1 decision is its own checkpoint",
                "auto-until-needed: the researcher batches checkpoints and stops only when it needs answers"]),
            "SETUP-reviewer": ("reviewer strategy", [
                "use reviewer (recommended): a reviewer pass before every stage gate",
                "skip reviewer: record the skip, accepted risk, and revisit trigger at each gate"]),
            "SETUP-gates": ("gate mode", [
                "real gates (recommended for real research): you decide every gate and checkpoint",
                "synthetic gates (framework tests only): the orchestrator takes the recommended option"]),
        }
        for key, (what, opts) in questions.items():
            body = "\n".join(f"{i}. {o}" for i, o in enumerate(opts, 1))
            (self.project / "inbox/pending" / f"{key}.md").write_text(
                f"# Pre-Planning setup: {what}\n\n- Type: setup\n- Stage: pre-planning\n- Raised by: orchestrator\n\n"
                f"## Decision needed\n\nChoose the {what} for this project.\n\n"
                f"## Proposal\n\nOption 1 is the default for real research.\n\n"
                f"## Evidence\n\nAgents: researcher = {roles['researcher']}, reviewer = {json.dumps(roles['reviewer'])} "
                f"(workflow.config.json).\n\n## Alternatives\n\nSee options.\n\n## Open objections\n\nnone\n\n"
                f"## Reversibility\n\nCan be changed later as a reconfiguration.\n\n## Options\n\n{body}\n\n"
                f"## Decision\n\n{inbox.DECISION_HINT}\n", encoding="utf-8")

    # ------------------------------------------------------------------ helpers

    @property
    def run_dir(self) -> Path:
        return self.project / "artifacts" / self.state["run_id"]

    @property
    def rel_run_dir(self) -> str:
        return str(self.run_dir.relative_to(self.root))

    def _next_revision(self, stage: str) -> int:
        """1 + the highest revision already used for this stage's handoff files."""
        used = [0]
        for p in self.run_dir.glob(f"*-{stage}*.md"):
            m = re.search(rf"-{stage}(?:-r(\d+))?\.md$", p.name)
            if m:
                used.append(int(m.group(1) or 1))
        return max(used) + 1

    def _files(self) -> dict:
        return prompts._files(self.state["stage"], self.state["revision"])

    def _save(self) -> None:
        self.state_path.parent.mkdir(parents=True, exist_ok=True)
        self.state_path.write_text(json.dumps(self.state, indent=2), encoding="utf-8")

    def _event(self, msg: str) -> None:
        self.state["history"].append(f"{date.today().isoformat()} {self.state['stage']}/{self.state['step']}: {msg}")
        self.print(f"[orchestrator] {msg}")

    def _log(self, stage, typ, decision, proposed_by, evidence, authorized_by, quality,
             alternatives="", objections="", status="active") -> str:
        return decision_log.append(self.project / "decision-log.md", {
            "date": date.today().isoformat(), "stage": stage, "type": typ, "decision": decision,
            "proposed_by": proposed_by, "evidence": evidence, "alternatives": alternatives,
            "objections": objections, "authorized_by": authorized_by, "quality": quality, "status": status,
        })

    def _adapter(self, name: str):
        if name not in self._adapters:
            self._adapters[name] = make_adapter(name, self.cfg["agents"][name])
        return self._adapters[name]

    def _ctx(self, reviewer_spec: dict = None) -> dict:
        s = self.state
        return {
            "stage": s["stage"], "revision": s["revision"], "project_dir": self.rel_project,
            "run_dir": self.rel_run_dir, "mode": s["settings"]["mode"], "reviewer": s["settings"]["reviewer"],
            "gates": s["settings"]["gates"], "notes": "\n".join(s["notes"]), "topic": s.get("topic", ""),
            "reviewer_output": (reviewer_spec or {}).get("reviewer_output", "file"),
        }

    def _log_path(self, label: str) -> Path:
        n = len(self.state["history"]) + 1
        return self.run_dir / "agent" / f"{n:03d}-{self.state['stage']}-{label}.log"

    # ------------------------------------------------------------------ main loop

    def run(self, max_steps: int = 50, until_stage: str = None) -> str:
        if self.state is None:
            raise RuntimeError("project not initialized; run `init` first")
        for _ in range(max_steps):
            if until_stage and STAGES.index(self.state["stage"]) > STAGES.index(until_stage):
                self._save()
                return WAITING
            if self.state["step"] == "done":
                self._save()
                return DONE
            status = self._handle_inbox()
            self._save()
            if status == WAITING:
                return WAITING
            if status == RUNNING:
                continue
            step = self.state["step"]
            try:
                getattr(self, f"_step_{step}")()
            except AgentError as exc:
                self._event(f"agent error: {exc}")
                self._raise_stuck(str(exc))
            self._save()
        return WAITING

    def _handle_inbox(self):
        items = inbox.pending(self.project / "inbox")
        if not items:
            return None
        synthetic = self.state["settings"]["gates"] == "synthetic"
        progressed = False
        for path in items:
            ans = inbox.decision_of(path)
            if ans is None:
                kind = inbox.header_field(path.read_text(encoding="utf-8"), "Type")
                if synthetic and kind != "human task":
                    opts = inbox.options(path.read_text(encoding="utf-8"))
                    ans = (opts[0] if opts else "approve", "synthetic: recommended option taken")
                    inbox.write_decision(path, ans[0], ans[1], "orchestrator (synthetic gate)")
                elif self.interactive:
                    ans = inbox.ask_terminal(path, self.input_fn, self.print)
                    if ans is None:
                        continue
                    inbox.write_decision(path, ans[0], ans[1], "user at terminal")
                else:
                    continue
            self._apply_answer(path, ans[0], ans[1], synthetic)
            progressed = True
        if inbox.pending(self.project / "inbox"):
            if not progressed:
                self.print("[orchestrator] waiting for you. Answer the files in "
                           f"{self.rel_project}/inbox/pending/ (fill the Decision section), then run again.")
                return WAITING
            return RUNNING
        return RUNNING if progressed else None

    def _apply_answer(self, path: Path, choice: str, notes: str, synthetic: bool) -> None:
        text = path.read_text(encoding="utf-8")
        kind = inbox.header_field(text, "Type").lower()
        quality = inbox.approval_quality(text, synthetic)
        who = "synthetic" if synthetic else "user"
        stage_label = self.state["stage"].capitalize()
        title = text.splitlines()[0].lstrip("# ").strip()
        evidence = f"{self.rel_project}/inbox/answered/{path.name}"
        archived = inbox.archive(path)

        if kind == "setup":
            key = path.stem.split("-", 1)[1]
            value = choice.split(" ")[0].split(":")[0].strip().lower()
            allowed = {"mode": {"step-by-step", "auto-until-needed"}, "reviewer": {"use", "skip"},
                       "gates": {"real", "synthetic"}}[key]
            if value in allowed:
                self.state["settings"][key] = value
            else:
                notes = f"(unrecognized answer '{choice}'; kept {self.state['settings'][key]}) {notes}"
            self._log("Pre-Planning", "tier-1 checkpoint", f"Setup {key}: {choice}. {notes}", "orchestrator",
                      evidence, who, quality)
            if not inbox.pending(self.project / "inbox"):
                self.state["step"] = "work"
            return

        if kind == "human task":
            self.state["human_tasks_done"].append(path.stem)
            self._event(f"human task {path.stem} marked {choice}")
            return

        if kind == "stuck":
            low = choice.lower()
            if low.startswith("stop"):
                self.state["step"] = "done"
            elif low.startswith("skip review"):
                self.state["settings"]["reviewer"] = "skip"
                self.state["step"] = "work"
                self._log(stage_label, "reconfiguration", f"Reviewer skipped after stuck state: {notes}",
                          "orchestrator", evidence, who, quality)
            self.state["attempts"] = 0
            if notes:
                self.state["notes"].append(f"User note after stuck state: {notes}")
            return

        if kind.startswith("tier-1"):
            did = self._log(stage_label, "tier-1 checkpoint", f"{title}: {choice}. {notes}".strip(),
                            "researcher", evidence, who, quality,
                            objections=inbox.section(text, "Open objections")[:300])
            self.state["notes"].append(f"Answer to {path.stem} ({did}): {choice}. {notes}".strip())
            return

        if kind.startswith("tier-2"):
            self._apply_gate(choice, notes, who, quality, evidence, archived)
            return

        self._event(f"unknown inbox item type '{kind}' in {path.name}; archived")

    def _apply_gate(self, choice, notes, who, quality, evidence, archived) -> None:
        stage = self.state["stage"]
        low = choice.lower()
        escalations = decision_log.open_escalations(self.project / "decision-log.md")
        objections = "; ".join(escalations) if escalations else "none"
        did = self._log(stage.capitalize(), "tier-2 gate", f"{stage.capitalize()} Gate: {choice}. {notes}".strip(),
                        "researcher", evidence, who, quality, objections=objections)
        self.state["notes"] = [f"Gate decision {did}: {choice}. {notes}".strip()] if notes else []
        self.state["attempts"] = 0
        if low.startswith(("approve", "finalize", "archive", "accept")):
            idx = STAGES.index(stage)
            if stage == "reviewing" or idx == len(STAGES) - 1:
                self.state["step"] = "done"
                self._event("Reviewing Gate approved: workflow complete. Fill run-notes.md evaluation if not done.")
            else:
                nxt = STAGES[idx + 1]
                self.state.update(stage=nxt, step="work", revision=self._next_revision(nxt))
                self._event(f"gate approved; starting {self.state['stage']}")
        elif low.startswith("backtrack"):
            target = next((s for s in STAGES if s in low), STAGES[max(0, STAGES.index(stage) - 1)])
            self.state.update(stage=target, step="work", revision=self._next_revision(target))
            self.state["notes"].append(f"Backtracked from {stage}: {choice}. {notes}")
            self._event(f"backtracking to {target}")
        elif low.startswith("terminate") or low.startswith("stop"):
            self.state["step"] = "done"
            self._event("workflow terminated at the gate")
        else:
            # revise, request more checks, or a free-form condition
            self.state.update(step="work", revision=self._next_revision(stage))
            self.state["notes"].append(f"User asked for revision at the {stage} gate: {choice}. {notes}")
            self._event(f"revising {stage} (revision {self.state['revision']})")

    # ------------------------------------------------------------------ steps

    def _run_researcher(self, label: str, prompt: str) -> bool:
        """Run the researcher. Returns False if a human task is now pending."""
        name = self.cfg["roles"]["researcher"]
        adapter = self._adapter(name)
        if adapter.kind == "human":
            return self._human_task("researcher", label, prompt)
        self._event(f"researcher ({name}) running: {label}")
        adapter.run_task(prompt, "researcher", self.root, self._log_path(f"researcher-{label}"))
        return True

    def _human_task(self, role: str, label: str, prompt: str) -> bool:
        task_id = f"TASK-{self.state['stage']}-{label}-r{self.state['revision']}"
        if task_id in self.state["human_tasks_done"]:
            return True
        (self.project / "inbox/pending" / f"{task_id}.md").write_text(
            f"# Task for you as {role}\n\n- Type: human task\n- Stage: {self.state['stage']}\n\n"
            f"## Instructions\n\n{prompt}\n\n## Options\n\n1. Done\n\n## Decision\n\n{inbox.DECISION_HINT}\n",
            encoding="utf-8")
        return False

    def _after_researcher(self, expect: str, next_step: str) -> None:
        if inbox.pending(self.project / "inbox"):
            self._event("researcher raised checkpoint(s)")
            return
        if (self.run_dir / expect).exists():
            self.state.update(step=next_step, attempts=0, notes=[])
            return
        self.state["attempts"] += 1
        limit = self.cfg.get("workflow", {}).get("max_attempts", 3)
        self._event(f"researcher stopped without {expect} (attempt {self.state['attempts']}/{limit})")
        if self.state["attempts"] >= limit:
            self._raise_stuck(f"the researcher stopped {limit} times without writing {expect}")
        else:
            self.state["notes"].append(f"Orchestrator: your last session ended without writing "
                                       f"{self.rel_run_dir}/{expect}. Finish the task or raise a checkpoint.")

    def _step_work(self) -> None:
        f = self._files()
        if not self._run_researcher("work", prompts.researcher_work(self._ctx())):
            return
        if self.state["settings"]["reviewer"] == "use":
            self._after_researcher(f["request"], "review")
        else:
            self._after_researcher(f["gate"], "gate")

    def _step_review(self) -> None:
        stage = self.state["stage"]
        name = reviewer_for(self.cfg, stage)
        spec = self.cfg["agents"][name]
        adapter = self._adapter(name)
        f = self._files()
        mode = review_mode_for(self.cfg, stage)
        critique = self.run_dir / f["critique"]
        self._event(f"reviewer ({name}, {mode}) running")
        if adapter.kind == "human":
            if not self._human_task("reviewer", "review", prompts.reviewer_cli(self._ctx(spec), "standard")):
                return
        elif adapter.kind in {"anthropic", "openai_compatible"}:
            self._review_api(adapter, mode, critique)
        else:
            self._review_cli(adapter, spec, mode, critique)
        if critique.exists():
            self.state.update(step="triage", attempts=0)
        else:
            self._raise_stuck(f"reviewer {name} finished without writing {f['critique']}")

    def _review_cli(self, adapter, spec, mode, critique: Path) -> None:
        f = self._files()
        framing = self.run_dir / f["framing"]
        ctx = self._ctx(spec)
        if mode != "blind":
            res = adapter.run_task(prompts.reviewer_cli(ctx, "standard"), "reviewer", self.root,
                                   self._log_path("reviewer"))
            if ctx["reviewer_output"] == "stdout":
                critique.write_text(res.text, encoding="utf-8")
            return
        # Blind: withhold the framing file during the independent pass.
        hold = Path(tempfile.mkdtemp(prefix="framing-hold-"))
        held = None
        if framing.exists():
            held = hold / framing.name
            shutil.move(str(framing), held)
        try:
            res = adapter.run_task(prompts.reviewer_cli(ctx, "independent"), "reviewer", self.root,
                                   self._log_path("reviewer-independent"))
            if ctx["reviewer_output"] == "stdout":
                critique.write_text(res.text, encoding="utf-8")
        finally:
            if held:
                shutil.move(str(held), framing)
            shutil.rmtree(hold, ignore_errors=True)
        if not critique.exists():
            return
        res = adapter.run_task(prompts.reviewer_cli(ctx, "follow-up"), "reviewer", self.root,
                               self._log_path("reviewer-follow-up"))
        if ctx["reviewer_output"] == "stdout":
            critique.write_text(replace_followup(critique.read_text(encoding="utf-8"), res.text),
                                encoding="utf-8")

    def _review_api(self, adapter, mode, critique: Path) -> None:
        f = self._files()
        stage = self.state["stage"]
        request_text = (self.run_dir / f["request"]).read_text(encoding="utf-8")
        framing_path = self.run_dir / f["framing"]
        framing_text = framing_path.read_text(encoding="utf-8") if framing_path.exists() else "(no framing file)"
        artifacts = self._collect_artifacts(request_text, exclude={framing_path.resolve()})
        system = prompts.reviewer_api_system(self.root, stage)
        if mode == "blind":
            independent = adapter.complete(system, prompts.reviewer_api_user(stage, request_text, artifacts, "independent"))
            followup = adapter.complete(system, prompts.reviewer_api_user(
                stage, request_text, artifacts, "follow-up", framing_text, independent))
            text = replace_followup(independent, followup)
        else:
            text = adapter.complete(system, prompts.reviewer_api_user(stage, request_text, artifacts, "standard", framing_text))
        critique.write_text(text, encoding="utf-8")
        (self._log_path("reviewer-api")).write_text(f"API reviewer {adapter.name}: wrote {critique.name}\n", encoding="utf-8")

    def _collect_artifacts(self, request_text: str, exclude: set) -> list:
        section = inbox.section(request_text, "Artifacts to Inspect")
        paths = []
        for line in section.splitlines():
            m = re.match(r"^\s*[-*]\s+`?([^`\s(]+)`?", line)
            if m:
                paths.append(m.group(1))
        for extra in ["decision-log.md", f"packages/{prompts.STAGE_DOCS[self.state['stage']][2]}"]:
            paths.append(f"{self.rel_project}/{extra}")
        seen, out, total = set(), [], 0
        limit = self.cfg.get("workflow", {}).get("max_review_context_chars", 1_500_000)
        for rel in paths:
            p = (self.root / rel).resolve()
            files = sorted(x for x in p.rglob("*") if x.is_file()) if p.is_dir() else [p]
            for fp in files:
                if fp in seen or fp in exclude or not fp.exists():
                    continue
                seen.add(fp)
                name = str(fp.relative_to(self.root))
                if fp.suffix not in TEXT_SUFFIXES:
                    out.append((name, f"[binary or non-text file, not included: {fp.stat().st_size} bytes]"))
                    continue
                text = fp.read_text(encoding="utf-8", errors="replace")
                total += len(text)
                out.append((name, text))
        if total > limit:
            raise AgentError(
                f"review context is {total} characters, above max_review_context_chars={limit}. "
                "Narrow the Artifacts to Inspect list or raise the limit; the orchestrator does not truncate.")
        return out

    def _step_triage(self) -> None:
        f = self._files()
        if not self._run_researcher("triage", prompts.researcher_triage(self._ctx())):
            return
        self._after_researcher(f["gate"], "gate")

    def _step_gate(self) -> None:
        f = self._files()
        gate_file = self.run_dir / f["gate"]
        text = gate_file.read_text(encoding="utf-8")
        if not re.search(r"^-\s*Type:", text, flags=re.M):
            text = re.sub(r"^(#.*\n)", r"\1\n- Type: tier-2 gate\n", text, count=1)
        if not re.search(r"^##\s+Decision\s*$", text, flags=re.M):
            text = text.rstrip() + f"\n\n## Decision\n\n{inbox.DECISION_HINT}\n"
        escalations = decision_log.open_escalations(self.project / "decision-log.md")
        if escalations:
            text = text.replace("## Options", "## Open escalations in the decision log\n\n" +
                                "\n".join(f"- {e}" for e in escalations) + "\n\n## Options", 1)
        target = self.project / "inbox/pending" / f"GATE-{self.state['stage']}-r{self.state['revision']}.md"
        target.write_text(text, encoding="utf-8")
        self.state["step"] = "gate_wait"
        self._event(f"{self.state['stage']} gate is ready for you")

    def _step_gate_wait(self) -> None:
        # Reached only if the gate file was removed without an answer.
        self.state["step"] = "gate"

    def _step_setup(self) -> None:
        if not inbox.pending(self.project / "inbox"):
            self.state["step"] = "work"

    def _raise_stuck(self, reason: str) -> None:
        sid = f"STUCK-{self.state['stage']}-{len(self.state['history'])}"
        (self.project / "inbox/pending" / f"{sid}.md").write_text(
            f"# The workflow is stuck\n\n- Type: stuck\n- Stage: {self.state['stage']}\n- Step: {self.state['step']}\n\n"
            f"## Decision needed\n\n{reason}\n\nAgent logs: {self.rel_run_dir}/agent/\n\n"
            "## Options\n\n1. retry: run the same step again (add notes for the agent below)\n"
            "2. skip review: continue without the reviewer pass (recorded as a reconfiguration)\n"
            "3. stop: end the run here\n\n"
            f"## Decision\n\n{inbox.DECISION_HINT}\n", encoding="utf-8")
        self.state["attempts"] = 0

    # ------------------------------------------------------------------ status

    def status(self) -> str:
        s = self.state
        lines = [f"project: {self.rel_project}", f"stage: {s['stage']}  step: {s['step']}  revision: {s['revision']}",
                 f"settings: {s['settings']}"]
        pend = inbox.pending(self.project / "inbox")
        lines.append("pending for you: " + (", ".join(p.name for p in pend) if pend else "none"))
        esc = decision_log.open_escalations(self.project / "decision-log.md")
        lines.append("open escalations: " + ("; ".join(esc) if esc else "none"))
        return "\n".join(lines)


def replace_followup(critique: str, followup: str) -> str:
    followup = followup.strip()
    if not followup.startswith("## Follow-Up Findings"):
        followup = "## Follow-Up Findings (blind mode only)\n\n" + followup
    pattern = r"^## Follow-Up Findings.*?(?=^## (?!Follow-Up)|\Z)"
    if re.search(pattern, critique, flags=re.M | re.S):
        return re.sub(pattern, lambda _m: followup + "\n\n", critique, count=1, flags=re.M | re.S)
    return critique.rstrip() + "\n\n" + followup + "\n"
