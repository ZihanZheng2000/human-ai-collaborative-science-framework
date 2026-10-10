"""Append authorization rows to a project's decision-log.md.

In orchestrated runs the engine, not an agent, writes every row whose
authority is a person (or a synthetic gate), so an agent cannot record an
approval that did not happen.
"""

import re
import shutil
from pathlib import Path

COLUMNS = [
    "id", "date", "stage", "type", "decision", "proposed_by", "evidence",
    "alternatives", "objections", "authorized_by", "quality", "status",
]


def ensure(log_path: Path, template: Path, project: str) -> None:
    if not log_path.exists():
        shutil.copy(template, log_path)
        text = log_path.read_text(encoding="utf-8").replace("<research-name>", project)
        # Drop the template's example row.
        text = re.sub(r"^\| D-1 \|  \|.*\n", "", text, flags=re.M)
        log_path.write_text(text, encoding="utf-8")


def next_id(text: str) -> str:
    ids = [int(n) for n in re.findall(r"^\|\s*D-(\d+)\s*\|", text, flags=re.M)]
    return f"D-{max(ids, default=0) + 1}"


def _cell(value: str) -> str:
    return " ".join(str(value).split()).replace("|", "/")


def append(log_path: Path, row: dict) -> str:
    text = log_path.read_text(encoding="utf-8")
    row = dict(row, id=next_id(text))
    line = "| " + " | ".join(_cell(row.get(c, "")) for c in COLUMNS) + " |"
    marker = "\n\n## Open Escalations"
    if marker in text:
        i = text.index(marker)
        text = text[:i] + "\n" + line + text[i:]
    else:
        text = text.rstrip() + "\n" + line + "\n"
    log_path.write_text(text, encoding="utf-8")
    return row["id"]


def open_escalations(log_path: Path) -> list:
    """Rows in the Open Escalations table that are not yet resolved."""
    if not log_path.exists():
        return []
    text = log_path.read_text(encoding="utf-8")
    m = re.search(r"^## Open Escalations\s*$(.*?)(?=^##\s|\Z)", text, flags=re.M | re.S)
    if not m:
        return []
    rows = []
    for line in m.group(1).splitlines():
        if not line.startswith("|") or line.startswith("|---") or line.startswith("| Escalation"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if cells and cells[0] and (len(cells) < 5 or not cells[4] or "pending" in cells[4].lower()):
            rows.append(cells[0])
    return rows
