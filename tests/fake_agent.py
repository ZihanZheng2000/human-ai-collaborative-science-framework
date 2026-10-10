"""A scripted stand-in for a CLI agent, used by the orchestrator tests.

Reads the orchestrator prompt from a file and writes the files a real agent
would write. Behaviour switches come from environment variables.
"""

import os
import re
import sys
from pathlib import Path


def field(prompt, name):
    m = re.search(rf"^{name}:\s*(.+)$", prompt, flags=re.M)
    return m.group(1).strip() if m else ""


def main():
    prompt = Path(sys.argv[1]).read_text(encoding="utf-8")
    role = sys.argv[3]
    if os.environ.get("FAKE_SILENT") == role:
        return
    if os.environ.get("FAKE_VANDAL") == role and "independent pass" not in prompt:
        Path("packages").mkdir(exist_ok=True)
        Path("packages/planning-package.md").write_text("edited by reviewer\n")
    if "--output-format" in sys.argv:
        # Session continuity: report a session id and remember what we were resumed with.
        resumed = sys.argv[sys.argv.index("--resume") + 1] if "--resume" in sys.argv else ""
        with open(".fake-sessions.log", "a") as fh:
            fh.write(f"{role} resume={resumed}\n")
    if role == "researcher":
        researcher(prompt)
    else:
        reviewer(prompt)
    if "--output-format" in sys.argv:
        import json
        print(json.dumps({"session_id": "sess-1", "result": "done"}))


def fw(prompt):
    m = re.search(r"Framework rules and templates \(read-only\): (.+)$", prompt, flags=re.M)
    return Path(m.group(1).strip())


def researcher(prompt):
    project = Path(field(prompt, "Project folder"))
    run_dir = Path(field(prompt, "Run directory"))
    stage_line = field(prompt, "Current stage")
    stage = stage_line.split()[0]
    rev = int(re.search(r"revision (\d+)", stage_line).group(1))
    sfx = "" if rev == 1 else f"-r{rev}"
    (project / "packages").mkdir(parents=True, exist_ok=True)
    if "step: respond to review" in prompt:
        gate = (fw(prompt) / "templates/gate-request.md").read_text(encoding="utf-8")
        gate = gate.replace("<Stage>", stage.capitalize()).replace("<planning / modeling / reporting / reviewing>", stage)
        gate = gate.replace("<what the user is asked to approve, and the recommended choice>", "Approve the package.")
        gate = gate.replace("<one paragraph and the package path>", "Did the work.")
        gate = gate.replace("- <three to five artifact paths most worth opening>", f"- {project}/packages/{stage}-package.md")
        gate = re.sub(r"<every escalated.*?\"none\" if none>", "none", gate, flags=re.S)
        gate = gate.replace("<other routes and what each would cause>", "revise")
        gate = gate.replace("<what happens next if approved, and how it could be reversed>", "next stage")
        (run_dir / f"gate-request-{stage}{sfx}.md").write_text(gate, encoding="utf-8")
        return
    answered = project / "inbox" / "answered" / f"CP-{stage}-1.md"
    if stage == "planning" and not answered.exists() and os.environ.get("FAKE_CHECKPOINT", "1") == "1":
        cp = (fw(prompt) / "templates/checkpoint-request.md").read_text(encoding="utf-8")
        cp = cp.replace("<short title>", "Research question").replace("<planning / modeling / reporting / reviewing>", "planning")
        for tag in ["one or two sentences", "what you recommend", "artifact paths", "other options",
                    "known objections", "how hard"]:
            cp = re.sub(rf"<{tag}[^>]*>", "filled", cp)
        cp = cp.replace("<recommended option>", "Use question A").replace("<alternative>", "Use question B")
        (project / "inbox" / "pending" / "CP-planning-1.md").write_text(cp, encoding="utf-8")
        return
    notes = re.search(r"Messages from the user or orchestrator for this session:\n(.*?)\n\n", prompt, re.S)
    (project / "packages" / f"{stage}-package.md").write_text(
        f"# {stage} package r{rev}\n\nnotes seen: {notes.group(1) if notes else ''}\n", encoding="utf-8")
    if "reviewer pass is skipped" in prompt:
        (run_dir / f"gate-request-{stage}{sfx}.md").write_text(
            f"# {stage} gate\n\n- Type: tier-2 gate\n\n## Options\n\n1. Approve\n2. Revise\n", encoding="utf-8")
        return
    (run_dir / f"review-request-{stage}{sfx}.md").write_text(
        f"# Review Request\n\n## Header\n\n- Stage: {stage}\n\n## Artifacts to Inspect\n\n"
        f"- {project}/packages/{stage}-package.md\n", encoding="utf-8")
    (run_dir / f"review-framing-{stage}{sfx}.md").write_text("# Framing\n\nSECRET-FRAMING\n", encoding="utf-8")


def reviewer(prompt):
    request = Path(field(prompt, "Review request"))
    run_dir = request.parent
    stage = field(prompt, "Stage").split()[0]
    rev = int(re.search(r"revision (\d+)", field(prompt, "Stage")).group(1))
    sfx = "" if rev == 1 else f"-r{rev}"
    critique = run_dir / f"reviewer-critique-{stage}{sfx}.md"
    framing = run_dir / f"review-framing-{stage}{sfx}.md"
    if "independent pass" in prompt:
        critique.write_text(f"# Critique\n\nframing visible: {'yes' if framing.exists() else 'no'}\n\n"
                            "## Findings\n\n| RVR-1 | minor |\n\n## Follow-Up Findings\n\npending second pass\n\n"
                            "## Overall Assessment\n\nok\n", encoding="utf-8")
    elif "follow-up pass" in prompt:
        text = critique.read_text(encoding="utf-8")
        text = text.replace("pending second pass", f"followed up; framing visible now: {'yes' if framing.exists() else 'no'}")
        critique.write_text(text, encoding="utf-8")
    else:
        critique.write_text(f"# Critique\n\n## Findings\n\n| XR-1 | minor |\n", encoding="utf-8")


if __name__ == "__main__":
    main()
