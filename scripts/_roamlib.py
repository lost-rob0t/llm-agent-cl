from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
ROAM = ROOT / "roam"
TREES = ("research", "design", "implement", "indexes")
SUBSTANTIVE = ("research", "design", "implementation", "specification", "provider", "architecture", "index", "operations")

META_RE = re.compile(r"^#\+([A-Za-z0-9_-]+):\s*(.*)$", re.M)
ID_RE = re.compile(r"^:ID:\s*(\S+)\s*$", re.M)
ID_LINK_RE = re.compile(r"\bid:([A-Za-z0-9._:-]+)")

@dataclass(frozen=True)
class OrgDoc:
    path: Path
    text: str
    metadata: dict[str, str]
    doc_id: str | None


def read_org(path: Path) -> OrgDoc:
    text = path.read_text(encoding="utf-8")
    metadata = {k.lower(): v.strip() for k, v in META_RE.findall(text)}
    match = ID_RE.search(text)
    return OrgDoc(path, text, metadata, match.group(1) if match else None)


def org_files(*trees: str) -> list[Path]:
    selected = trees or TREES
    out: list[Path] = []
    for tree in selected:
        base = ROAM / tree
        if base.exists():
            out.extend(sorted(base.rglob("*.org")))
    return out


def project_names() -> set[str]:
    names: set[str] = set()
    for tree in TREES:
        base = ROAM / tree
        if not base.exists():
            continue
        names.update(p.name for p in base.iterdir() if p.is_dir())
    return names


def approval_present(text: str) -> bool:
    return "* Approval Table" in text and "| Approval area | Required authority | State | Evidence required | Evidence reference |" in text


def changelog_present(text: str) -> bool:
    return "* Changelog" in text and "| Date | Change | Author or actor | Evidence |" in text


def glossary_present(text: str) -> bool:
    return "* Footnotes and Glossary" in text
