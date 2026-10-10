"""Human nodes: checkpoint and gate files in <project>/inbox/.

An agent or the engine writes a request to inbox/pending/<ID>.md. A person
answers it either at the terminal (the engine fills the Decision section) or
by editing the file and re-running the orchestrator. Answered files move to
inbox/answered/.
"""

import re
import shutil
from datetime import date
from pathlib import Path

# Sections a request must show for an approval to count as substantive
# (docs/decision-rights.md#substantive-versus-nominal-approval).
SUBSTANTIVE_SECTIONS = {
    "proposal": ["Proposal", "Decision needed"],
    "evidence": ["Evidence", "Evidence to inspect"],
    "alternatives": ["Alternatives"],
    "objections": ["Open objections"],
    "consequences": ["Reversibility", "Consequence of approval", "Consequences"],
}

DECISION_HINT = "<!-- Write the option number or label on the first line; add notes below. -->"


def section(text: str, heading: str) -> str:
    pattern = rf"^##\s+{re.escape(heading)}\s*$(.*?)(?=^##\s|\Z)"
    m = re.search(pattern, text, flags=re.M | re.S | re.I)
    if not m:
        return ""
    return re.sub(r"<!--.*?-->", "", m.group(1), flags=re.S).strip()


def options(text: str) -> list:
    body = section(text, "Options")
    return [m.group(1).strip() for m in re.finditer(r"^\s*\d+[.)]\s+(.+)$", body, flags=re.M)]


def header_field(text: str, field: str) -> str:
    m = re.search(rf"^-\s*{re.escape(field)}:\s*(.+)$", text, flags=re.M | re.I)
    return m.group(1).strip() if m else ""


def pending(inbox: Path) -> list:
    folder = inbox / "pending"
    return sorted(folder.glob("*.md")) if folder.exists() else []


def decision_of(path: Path):
    """Return (choice, notes) if the Decision section is filled, else None."""
    text = path.read_text(encoding="utf-8")
    body = section(text, "Decision")
    if not body:
        return None
    first, _, rest = body.partition("\n")
    opts = options(text)
    choice = first.strip()
    if choice.isdigit() and 1 <= int(choice) <= len(opts):
        choice = opts[int(choice) - 1]
    return choice, rest.strip()


def write_decision(path: Path, choice: str, notes: str, by: str) -> None:
    text = path.read_text(encoding="utf-8")
    entry = f"{choice}\n{notes}\n\n_Recorded {date.today().isoformat()} by {by}._".strip()
    if re.search(r"^##\s+Decision\s*$", text, flags=re.M):
        text = re.sub(r"(^##\s+Decision\s*$)(.*?)(?=^##\s|\Z)", lambda m: f"{m.group(1)}\n\n{entry}\n\n",
                      text, count=1, flags=re.M | re.S)
    else:
        text = text.rstrip() + f"\n\n## Decision\n\n{entry}\n"
    path.write_text(text, encoding="utf-8")


def archive(path: Path) -> Path:
    dest = path.parent.parent / "answered" / path.name
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(path), dest)
    return dest


def approval_quality(text: str, synthetic: bool) -> str:
    if synthetic:
        return "synthetic"
    missing = [key for key, names in SUBSTANTIVE_SECTIONS.items()
               if not any(section(text, n) for n in names)]
    if not options(text):
        missing.append("options")
    return "substantive" if not missing else "nominal: missing " + ", ".join(missing)


def ask_terminal(path: Path, input_fn=input, print_fn=print):
    """Show a request and read the answer from the terminal."""
    text = path.read_text(encoding="utf-8")
    opts = options(text)
    print_fn("\n" + "=" * 72)
    print_fn(re.sub(r"^##\s+Decision\s*$.*", "", text, flags=re.M | re.S).rstrip())
    print_fn("-" * 72)
    for i, opt in enumerate(opts, 1):
        print_fn(f"  {i}. {opt}")
    print_fn("  Type a number, or your own decision. 'later' leaves it in the inbox.")
    while True:
        raw = input_fn("decision> ").strip()
        if not raw:
            continue
        if raw.lower() == "later":
            return None
        if raw.isdigit() and 1 <= int(raw) <= len(opts):
            choice = opts[int(raw) - 1]
        else:
            choice = raw
        notes = input_fn("notes (optional)> ").strip()
        return choice, notes
