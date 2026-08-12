#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
from _roamlib import ROAM, TREES, project_names


def main() -> int:
    parser = argparse.ArgumentParser(description="Mirror project directories across canonical roam trees.")
    parser.add_argument("--check", action="store_true", help="fail instead of creating missing directories")
    args = parser.parse_args()

    for tree in TREES:
        (ROAM / tree).mkdir(parents=True, exist_ok=True)

    projects = project_names()
    missing: list[Path] = []
    for project in sorted(projects):
        for tree in TREES:
            path = ROAM / tree / project
            if not path.exists():
                missing.append(path)

    if args.check:
        for path in missing:
            print(f"missing mirrored directory: {path.relative_to(ROAM.parent)}")
        return 1 if missing else 0

    for path in missing:
        path.mkdir(parents=True, exist_ok=True)
        print(f"created {path.relative_to(ROAM.parent)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
