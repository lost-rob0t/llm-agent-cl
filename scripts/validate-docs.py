#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path
from _roamlib import ID_LINK_RE, approval_present, changelog_present, glossary_present, org_files, read_org

REQUIRED_META = ("title", "description", "status", "filetags")
ALLOWED_APPROVAL = {"PENDING", "NOT STARTED", "APPROVED", "REJECTED", "SUPERSEDED", "NOT APPLICABLE"}
APPROVAL_HEADER = "| Approval area | Required authority | State | Evidence required | Evidence reference |"


def changed_paths(base: str) -> set[Path]:
    proc = subprocess.run(
        ["git", "diff", "--name-only", f"{base}...HEAD", "--", "roam"],
        text=True,
        capture_output=True,
        check=True,
    )
    return {Path(line.strip()) for line in proc.stdout.splitlines() if line.strip()}


def approval_states(text: str) -> list[str]:
    lines = text.splitlines()
    try:
        start = lines.index(APPROVAL_HEADER)
    except ValueError:
        return []
    states: list[str] = []
    for line in lines[start + 2 :]:
        if not line.startswith("|"):
            break
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) >= 3:
            states.append(cells[2])
    return states


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--changed-since")
    parser.add_argument("--audit-date")
    args = parser.parse_args()

    all_docs = [read_org(path) for path in org_files()]
    selected = all_docs
    if args.changed_since:
        changed = changed_paths(args.changed_since)
        selected = [doc for doc in all_docs if doc.path.relative_to(Path.cwd()) in changed]

    errors: list[str] = []
    ids: dict[str, Path] = {}
    for doc in all_docs:
        rel = doc.path.relative_to(Path.cwd())
        if not doc.doc_id:
            errors.append(f"{rel}: missing :ID:")
        elif doc.doc_id in ids:
            errors.append(f"{rel}: duplicate ID {doc.doc_id} also in {ids[doc.doc_id]}")
        else:
            ids[doc.doc_id] = rel

    known = set(ids)
    for doc in selected:
        rel = doc.path.relative_to(Path.cwd())
        for key in REQUIRED_META:
            if not doc.metadata.get(key):
                errors.append(f"{rel}: missing #+{key}:")
        if not approval_present(doc.text):
            errors.append(f"{rel}: missing approval table")
        else:
            states = approval_states(doc.text)
            if not states:
                errors.append(f"{rel}: approval table has no rows")
            for state in states:
                if state not in ALLOWED_APPROVAL:
                    errors.append(f"{rel}: invalid approval state {state!r}")
        if not changelog_present(doc.text):
            errors.append(f"{rel}: missing changelog")
        if not glossary_present(doc.text):
            errors.append(f"{rel}: missing Footnotes and Glossary")
        for target in ID_LINK_RE.findall(doc.text):
            if target not in known:
                errors.append(f"{rel}: unresolved id:{target}")

    if errors:
        for error in errors:
            print(error)
        return 1
    print(f"validated {len(selected)} Org documents ({len(all_docs)} total IDs indexed)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
