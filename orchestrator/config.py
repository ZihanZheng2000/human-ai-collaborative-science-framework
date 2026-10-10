"""Load and validate workflow.config.json."""

import json
from pathlib import Path

from . import STAGES

AGENT_KINDS = {"cli", "anthropic", "openai_compatible", "human"}
# Kinds that can edit files and run code in the workspace.
WORKSPACE_KINDS = {"cli", "human"}


class ConfigError(Exception):
    pass


def load_config(path: Path) -> dict:
    if not path.exists():
        raise ConfigError(f"config not found: {path} (copy workflow.config.example.json)")
    cfg = json.loads(path.read_text(encoding="utf-8"))
    validate(cfg)
    return cfg


def validate(cfg: dict) -> None:
    agents = cfg.get("agents")
    roles = cfg.get("roles")
    if not isinstance(agents, dict) or not agents:
        raise ConfigError("config needs a non-empty 'agents' object")
    if not isinstance(roles, dict) or "researcher" not in roles or "reviewer" not in roles:
        raise ConfigError("config 'roles' must name a 'researcher' and a 'reviewer'")

    for name, spec in agents.items():
        kind = spec.get("kind")
        if kind not in AGENT_KINDS:
            raise ConfigError(f"agent '{name}': kind must be one of {sorted(AGENT_KINDS)}")
        if kind == "cli" and not (spec.get("command") or spec.get("role_commands")):
            raise ConfigError(f"agent '{name}': cli agents need 'command' or 'role_commands'")
        if kind in {"anthropic", "openai_compatible"} and not spec.get("model"):
            raise ConfigError(f"agent '{name}': API agents need 'model'")

    researcher = roles["researcher"]
    if researcher not in agents:
        raise ConfigError(f"researcher agent '{researcher}' is not defined in 'agents'")
    if agents[researcher]["kind"] not in WORKSPACE_KINDS:
        raise ConfigError(
            f"researcher agent '{researcher}' is kind '{agents[researcher]['kind']}'; the researcher "
            "must edit files and run code, so it must be a 'cli' or 'human' agent. API agents "
            "can currently serve as reviewers only."
        )

    for stage in STAGES:
        name = reviewer_for(cfg, stage)
        if name not in agents:
            raise ConfigError(f"reviewer for stage '{stage}' ('{name}') is not defined in 'agents'")

    wf = cfg.get("workflow", {})
    if wf.get("mode", "step-by-step") not in {"step-by-step", "auto-until-needed"}:
        raise ConfigError("workflow.mode must be 'step-by-step' or 'auto-until-needed'")
    if wf.get("gates", "real") not in {"real", "synthetic"}:
        raise ConfigError("workflow.gates must be 'real' or 'synthetic'")
    if wf.get("reviewer", "use") not in {"use", "skip"}:
        raise ConfigError("workflow.reviewer must be 'use' or 'skip'")


def reviewer_for(cfg: dict, stage: str) -> str:
    spec = cfg["roles"]["reviewer"]
    if isinstance(spec, str):
        return spec
    return spec.get(stage, spec.get("default"))


def review_mode_for(cfg: dict, stage: str) -> str:
    modes = cfg.get("workflow", {}).get("review_modes", {})
    return modes.get(stage, "blind" if stage == "reviewing" else "standard")
