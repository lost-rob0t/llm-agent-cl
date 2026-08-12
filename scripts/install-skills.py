#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description="Install the repository skill pack into a selected directory.")
    parser.add_argument("destination", type=Path)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    manifest = json.loads((ROOT / "skills" / "manifest.json").read_text(encoding="utf-8"))
    args.destination.mkdir(parents=True, exist_ok=True)
    for skill in manifest["skills"]:
        src = ROOT / skill["path"]
        dst = args.destination / Path(skill["path"]).parent.name / "SKILL.md"
        if dst.exists() and not args.force:
            raise SystemExit(f"exists: {dst}; use --force")
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        print(dst)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
