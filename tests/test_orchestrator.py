"""End-to-end tests for the orchestrator with scripted agents.

Run: python -m unittest discover -s tests
"""

import os
import re
import shutil
import sys
import tempfile
import unittest
from contextlib import contextmanager
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from orchestrator import inbox  # noqa: E402
from orchestrator.adapters import AgentError, AnthropicAdapter  # noqa: E402
from orchestrator.config import ConfigError, validate  # noqa: E402
from orchestrator.engine import DONE, WAITING, Engine  # noqa: E402

FAKE = str(REPO / "tests" / "fake_agent.py")


def fake_cli(role):
    return {"kind": "cli", "command": [sys.executable, FAKE, "{prompt_file}", "--role", role]}


def config(gates="synthetic", reviewer_agent=None, mode="step-by-step", reviewer="use"):
    return {
        "agents": {"fake-researcher": fake_cli("researcher"), "fake-reviewer": fake_cli("reviewer"),
                   **({reviewer_agent[0]: reviewer_agent[1]} if reviewer_agent else {})},
        "roles": {"researcher": "fake-researcher",
                  "reviewer": reviewer_agent[0] if reviewer_agent else "fake-reviewer"},
        "workflow": {"mode": mode, "reviewer": reviewer, "gates": gates, "review_modes": {"reviewing": "blind"}},
    }


class Sandbox:
    """A throwaway repository root with the framework's docs and templates."""

    def __init__(self):
        self.root = Path(tempfile.mkdtemp(prefix="orch-test-"))
        shutil.copytree(REPO / "docs", self.root / "docs")
        shutil.copytree(REPO / "templates", self.root / "templates")
        self.project = self.root / "research" / "demo"

    def engine(self, cfg, **kw):
        return Engine(self.root, cfg, self.project, print_fn=lambda *a: None, **kw)

    def log(self):
        return (self.project / "decision-log.md").read_text(encoding="utf-8")

    def close(self):
        shutil.rmtree(self.root, ignore_errors=True)


@contextmanager
def env(**values):
    old = {k: os.environ.get(k) for k in values}
    os.environ.update(values)
    try:
        yield
    finally:
        for k, v in old.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v


def answer(project, name, choice, notes=""):
    inbox.write_decision(project / "inbox" / "pending" / name, choice, notes, "test user")


class SyntheticRunTest(unittest.TestCase):
    def test_full_run_reaches_done_with_logged_decisions(self):
        sb = Sandbox()
        try:
            eng = sb.engine(config("synthetic"), interactive=False)
            eng.init_project("test topic", run_id="r1")
            self.assertEqual(eng.run(max_steps=60), DONE)
            log = sb.log()
            self.assertEqual(len(re.findall(r"\| tier-2 gate \|", log)), 4)
            self.assertIn("Research question", log)  # the planning checkpoint
            self.assertNotIn("substantive", log)  # synthetic run: no substantive approvals
            run = sb.project / "artifacts" / "r1"
            for stage in ["planning", "modeling", "reporting", "reviewing"]:
                self.assertTrue((run / f"reviewer-critique-{stage}.md").exists(), stage)
            # Blind review at Reviewing: framing withheld in pass 1, shown in pass 2.
            crit = (run / "reviewer-critique-reviewing.md").read_text()
            self.assertIn("framing visible: no", crit)
            self.assertIn("framing visible now: yes", crit)
            self.assertTrue((run / "review-framing-reviewing.md").exists())
            # Checkpoint answer reached the researcher.
            self.assertIn("Answer to CP-planning-1", (sb.project / "packages/planning-package.md").read_text())
        finally:
            sb.close()


class RealGateTest(unittest.TestCase):
    def test_inbox_mode_pauses_at_each_human_node(self):
        sb = Sandbox()
        try:
            cfg = config("real")
            eng = sb.engine(cfg, interactive=False)
            eng.init_project("test topic", run_id="r1")
            self.assertEqual(eng.run(), WAITING)
            pend = sorted(p.name for p in inbox.pending(sb.project / "inbox"))
            self.assertEqual(pend, ["SETUP-gates.md", "SETUP-mode.md", "SETUP-reviewer.md"])
            answer(sb.project, "SETUP-mode.md", "1")
            answer(sb.project, "SETUP-reviewer.md", "1")
            answer(sb.project, "SETUP-gates.md", "1")

            eng = sb.engine(cfg, interactive=False)
            self.assertEqual(eng.run(), WAITING)  # stops at the researcher's checkpoint
            self.assertEqual([p.name for p in inbox.pending(sb.project / "inbox")], ["CP-planning-1.md"])
            answer(sb.project, "CP-planning-1.md", "2", "prefer B")

            eng = sb.engine(cfg, interactive=False)
            self.assertEqual(eng.run(), WAITING)  # stops at the Planning Gate
            self.assertEqual([p.name for p in inbox.pending(sb.project / "inbox")], ["GATE-planning-r1.md"])
            self.assertIn("Use question B", sb.log())
            answer(sb.project, "GATE-planning-r1.md", "Revise Planning", "tighten scope")

            eng = sb.engine(cfg, interactive=False)
            self.assertEqual(eng.run(), WAITING)  # revision 2 gate
            self.assertEqual([p.name for p in inbox.pending(sb.project / "inbox")], ["GATE-planning-r2.md"])
            self.assertTrue((sb.project / "artifacts/r1/review-request-planning-r2.md").exists())
            self.assertIn("tighten scope", (sb.project / "packages/planning-package.md").read_text())
            answer(sb.project, "GATE-planning-r2.md", "1")

            eng = sb.engine(cfg, interactive=False)
            self.assertEqual(eng.run(), WAITING)
            self.assertEqual(eng.state["stage"], "modeling")
            log = sb.log()
            self.assertIn("Planning Gate: Approve for <next stage>", log)
            self.assertRegex(log, r"Planning Gate: Revise Planning.*\| user \| substantive \|")
            self.assertRegex(log, r"Setup mode.*\| user \|")
        finally:
            sb.close()

    def test_terminal_answers(self):
        sb = Sandbox()
        try:
            answers = iter(["1", "", "1", "", "1", "", "1", "", "terminate", "no data"])
            eng = sb.engine(config("real"), interactive=True, input_fn=lambda _p: next(answers))
            eng.init_project("test topic", run_id="r1")
            self.assertEqual(eng.run(), DONE)
            self.assertIn("Planning Gate: terminate. no data", sb.log())
        finally:
            sb.close()


class StuckAndSkipTest(unittest.TestCase):
    def test_silent_researcher_raises_stuck_item(self):
        sb = Sandbox()
        try:
            with env(FAKE_SILENT="researcher"):
                eng = sb.engine(config("real"), interactive=False)
                eng.init_project("test topic", run_id="r1", use_config_defaults=True)
                self.assertEqual(eng.run(), WAITING)
            names = [p.name for p in inbox.pending(sb.project / "inbox")]
            self.assertEqual(len(names), 1)
            self.assertTrue(names[0].startswith("STUCK-planning"))
            self.assertIn("nominal: setup taken from the config file", sb.log())
        finally:
            sb.close()

    def test_skip_reviewer_goes_straight_to_gate(self):
        sb = Sandbox()
        try:
            with env(FAKE_CHECKPOINT="0"):
                eng = sb.engine(config("synthetic", reviewer="skip"), interactive=False)
                eng.init_project("test topic", run_id="r1")
                self.assertEqual(eng.run(max_steps=40), DONE)
            self.assertFalse(list((sb.project / "artifacts/r1").glob("reviewer-critique-*")))
        finally:
            sb.close()


class _FakeStream:
    def __init__(self, text):
        block = type("B", (), {"type": "text", "text": text})()
        self.message = type("M", (), {"content": [block], "stop_reason": "end_turn", "stop_details": None})()

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def get_final_message(self):
        return self.message


class _FakeAnthropic:
    def __init__(self):
        self.calls = []
        outer = self

        class Msgs:
            def stream(self, **params):
                outer.calls.append(params)
                user = params["messages"][0]["content"]
                if "follow-up pass" in user:
                    return _FakeStream("## Follow-Up Findings\n\nsaw framing: " +
                                       ("yes" if "SECRET-FRAMING" in user else "no"))
                return _FakeStream("# Critique\n\nsaw framing: " + ("yes" if "SECRET-FRAMING" in user else "no") +
                                   "\n\n## Follow-Up Findings\n\npending second pass\n\n## Overall Assessment\n\nok\n")

        self.beta = type("Beta", (), {"messages": Msgs()})()


class ApiReviewerTest(unittest.TestCase):
    def test_blind_api_review_withholds_framing_in_first_call(self):
        sb = Sandbox()
        try:
            fake = _FakeAnthropic()
            spec = {"kind": "anthropic", "model": "claude-opus-5-5"}
            cfg = config("synthetic", reviewer_agent=("claude-api", spec))
            cfg["workflow"]["review_modes"] = {"planning": "blind"}
            adapters = {"claude-api": AnthropicAdapter("claude-api", spec, client=fake)}
            with env(FAKE_CHECKPOINT="0"):
                eng = sb.engine(cfg, interactive=False, adapters=adapters)
                eng.init_project("test topic", run_id="r1")
                eng.run(max_steps=4)
            crit = (sb.project / "artifacts/r1/reviewer-critique-planning.md").read_text()
            self.assertIn("saw framing: no", crit.split("## Follow-Up")[0])
            self.assertIn("## Follow-Up Findings\n\nsaw framing: yes", crit)
            first = fake.calls[0]
            self.assertEqual(first["model"], "claude-opus-5-5")
            self.assertEqual(first["thinking"], {"type": "adaptive"})
            self.assertEqual(first["fallbacks"], "default")
            self.assertIn("planning-package.md", first["messages"][0]["content"])
        finally:
            sb.close()

    def test_refusal_raises(self):
        fake = _FakeAnthropic()
        msg = type("M", (), {"content": [], "stop_reason": "refusal", "stop_details": "cyber"})()
        fake.beta.messages.stream = lambda **p: _Refused(msg)
        adapter = AnthropicAdapter("a", {"model": "claude-opus-5-5"}, client=fake)
        with self.assertRaises(AgentError):
            adapter.complete("s", "u")


class _Refused(_FakeStream):
    def __init__(self, message):
        self.message = message


class ConfigSnapshotTest(unittest.TestCase):
    def test_snapshot_and_reconfiguration_logged(self):
        sb = Sandbox()
        try:
            cfg = config("real")
            eng = sb.engine(cfg, interactive=False, config_source="custom.json")
            eng.init_project("t", run_id="r1", use_config_defaults=True)
            self.assertTrue((sb.project / ".workflow/config.json").exists())
            self.assertIn("Setup from custom.json", sb.log())
            cfg2 = config("real")
            cfg2["agents"]["other"] = fake_cli("reviewer")
            cfg2["roles"]["reviewer"] = "other"
            with env(FAKE_SILENT="researcher"):
                sb.engine(cfg2, interactive=False).run(max_steps=1)
            self.assertRegex(sb.log(), r"\| reconfiguration \| Agent configuration changed")
        finally:
            sb.close()


class ExternalProjectTest(unittest.TestCase):
    def test_project_outside_framework_repo(self):
        sb = Sandbox()
        outside = Path(tempfile.mkdtemp(prefix="my-study-"))
        try:
            sb.project = outside / "study"
            eng = sb.engine(config("synthetic"), interactive=False)
            eng.init_project("t", run_id="r1")
            self.assertEqual(eng.run(max_steps=60), DONE)
            self.assertTrue((sb.project / "packages/reviewing-package.md").exists())
            pointer = (sb.project / "CLAUDE.md").read_text()
            self.assertIn(str(sb.root), pointer)
            self.assertIn("inbox/answered/", sb.log())  # evidence paths are project-relative
        finally:
            sb.close()
            shutil.rmtree(outside, ignore_errors=True)

    def test_existing_instruction_file_not_overwritten(self):
        sb = Sandbox()
        outside = Path(tempfile.mkdtemp(prefix="my-study-"))
        try:
            sb.project = outside / "study"
            sb.project.mkdir()
            (sb.project / "CLAUDE.md").write_text("mine")
            sb.engine(config("synthetic"), interactive=False).init_project("t", run_id="r1")
            self.assertEqual((sb.project / "CLAUDE.md").read_text(), "mine")
        finally:
            sb.close()
            shutil.rmtree(outside, ignore_errors=True)


class ReviewerGuardTest(unittest.TestCase):
    def test_reviewer_editing_files_is_stopped(self):
        sb = Sandbox()
        try:
            with env(FAKE_VANDAL="reviewer", FAKE_CHECKPOINT="0"):
                eng = sb.engine(config("real"), interactive=False)
                eng.init_project("t", run_id="r1", use_config_defaults=True)
                self.assertEqual(eng.run(), WAITING)
            stuck = [p for p in inbox.pending(sb.project / "inbox") if p.name.startswith("STUCK")]
            self.assertEqual(len(stuck), 1)
            self.assertIn("planning-package.md", stuck[0].read_text())
            self.assertEqual(eng.state["step"], "review")
        finally:
            sb.close()


class SessionContinuityTest(unittest.TestCase):
    def test_researcher_session_resumed_within_stage_only(self):
        sb = Sandbox()
        try:
            cfg = config("synthetic")
            cfg["agents"]["fake-researcher"]["session"] = {
                "within": "stage", "start_args": ["--output-format", "json"],
                "resume_args": ["--resume", "{session_id}"]}
            eng = sb.engine(cfg, interactive=False)
            eng.init_project("t", run_id="r1")
            eng.run(max_steps=60)
            calls = (sb.project / ".fake-sessions.log").read_text().splitlines()
            self.assertEqual(calls[0], "researcher resume=")          # first planning call
            self.assertEqual(calls[1], "researcher resume=sess-1")    # after the checkpoint, same stage
            stages = [h for h in eng.state["history"] if "running: work" in h]
            modeling_first = next(i for i, h in enumerate(stages) if "modeling/" in h)
            self.assertNotIn("resuming", stages[modeling_first])      # new stage, new session
        finally:
            sb.close()


class ReviewOnlyTest(unittest.TestCase):
    def test_review_command_on_manual_project(self):
        sb = Sandbox()
        try:
            run = sb.project / "artifacts" / "m1"
            run.mkdir(parents=True)
            (sb.project / "packages").mkdir()
            (sb.project / "packages/planning-package.md").write_text("pkg")
            (run / "review-request-planning.md").write_text("# Review Request\n\n## Artifacts to Inspect\n\n- packages/planning-package.md\n")
            (run / "review-framing-planning.md").write_text("framing")
            eng = sb.engine(config("real"), interactive=False)
            critique = eng.review_only("planning", run_id="m1")
            self.assertTrue(critique.exists())
            self.assertFalse((sb.project / ".workflow/state.json").exists())
        finally:
            sb.close()


class ConfigTest(unittest.TestCase):
    def test_api_researcher_rejected(self):
        cfg = config()
        cfg["agents"]["api"] = {"kind": "anthropic", "model": "claude-opus-5-5"}
        cfg["roles"]["researcher"] = "api"
        with self.assertRaises(ConfigError):
            validate(cfg)

    def test_example_configs_valid(self):
        import json
        for name in ["workflow.config.json", "workflow.config.example.json"]:
            validate(json.loads((REPO / name).read_text()))


if __name__ == "__main__":
    unittest.main()
