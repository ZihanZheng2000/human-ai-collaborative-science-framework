"""Command line: python -m orchestrator <command> ...

  init <project-dir>      create a project folder and ask the setup questions
  run <project-dir>       run the workflow until it needs a person or finishes
  status <project-dir>    show stage, step, pending decisions, open escalations
  review <project-dir> --stage S
                          run only the reviewer pass on an existing review request
                          (for manual runs; does not advance the workflow)

The project folder can be anywhere; agents run inside it.

Exit codes for `run`: 0 finished, 2 waiting for a person, 1 error.
"""

import argparse
import sys
from pathlib import Path

from .config import ConfigError, load_config
from .engine import DONE, Engine

REPO_ROOT = Path(__file__).resolve().parent.parent


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="python -m orchestrator", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", type=Path, default=REPO_ROOT / "workflow.config.json")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p_init = sub.add_parser("init")
    p_init.add_argument("project", type=Path)
    p_init.add_argument("--topic", required=True,
                        help="the research request in the user's own words (quoted)")
    p_init.add_argument("--run-id")
    p_init.add_argument("--use-config-defaults", action="store_true",
                        help="take workflow mode, reviewer strategy, and gate mode from the config "
                             "instead of asking (recorded as a nominal approval)")
    p_run = sub.add_parser("run")
    p_run.add_argument("project", type=Path)
    p_run.add_argument("--inbox-only", action="store_true",
                       help="do not ask at the terminal; leave decisions in the inbox and exit")
    p_run.add_argument("--max-steps", type=int, default=50)
    p_run.add_argument("--until", choices=["planning", "modeling", "reporting", "reviewing"],
                       help="stop once this stage's gate is approved")
    p_status = sub.add_parser("status")
    p_status.add_argument("project", type=Path)
    p_review = sub.add_parser("review")
    p_review.add_argument("project", type=Path)
    p_review.add_argument("--stage", required=True, choices=["planning", "modeling", "reporting", "reviewing"])
    p_review.add_argument("--revision", type=int, default=1)
    p_review.add_argument("--run-id", help="needed if the project was not started with `init`")
    args = ap.parse_args(argv)

    try:
        cfg = load_config(args.config)
    except ConfigError as exc:
        print(f"config error: {exc}", file=sys.stderr)
        return 1
    project = args.project.expanduser()
    project = project if project.is_absolute() else (Path.cwd() / project)
    interactive = args.cmd == "run" and not args.inbox_only and sys.stdin.isatty()
    try:
        source = str(args.config.resolve().relative_to(REPO_ROOT))
    except ValueError:
        source = str(args.config)
    engine = Engine(REPO_ROOT, cfg, project, interactive=interactive, config_source=source)

    if args.cmd == "init":
        if engine.state is not None:
            print(f"{args.project} is already initialized; use `run` or `status`.")
            return 1
        engine.init_project(args.topic, run_id=args.run_id, use_config_defaults=args.use_config_defaults)
        print(f"initialized {engine.rel_project}. Next: python -m orchestrator run {args.project}")
        return 0
    if args.cmd == "review":
        try:
            critique = engine.review_only(args.stage, args.revision, args.run_id)
        except RuntimeError as exc:
            print(f"review failed: {exc}", file=sys.stderr)
            return 1
        print(f"critique: {critique}" if critique.exists() else "no critique was written; see inbox/pending/")
        return 0 if critique.exists() else 2
    if engine.state is None:
        print(f"{args.project} is not initialized; run `init` first.", file=sys.stderr)
        return 1
    if args.cmd == "status":
        print(engine.status())
        return 0
    result = engine.run(max_steps=args.max_steps, until_stage=args.until)
    print(engine.status())
    return 0 if result == DONE else 2


if __name__ == "__main__":
    sys.exit(main())
