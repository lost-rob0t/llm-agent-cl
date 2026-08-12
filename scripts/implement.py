#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
from pathlib import Path
from _roamlib import ROAM


def active(project_dir: Path) -> list[Path]:
    return sorted(p for p in project_dir.glob("*.org") if p.is_file())


def main() -> int:
    parser = argparse.ArgumentParser(description="Activate exactly one canonical design for implementation.")
    parser.add_argument("design", nargs="?")
    parser.add_argument("--status", action="store_true")
    args = parser.parse_args()

    if args.status:
        for project_dir in sorted((ROAM / "implement").glob("*")):
            if project_dir.is_dir():
                items = active(project_dir)
                print(f"{project_dir.name}: {items[0].name if items else '-'}")
        return 0

    if not args.design:
        parser.error("design path is required unless --status is used")
    source = Path(args.design).resolve()
    design_root = (ROAM / "design").resolve()
    if design_root not in source.parents or source.suffix != ".org":
        raise SystemExit("design must be an Org file under roam/design/<project>/")
    project = source.parent.name
    target_dir = ROAM / "implement" / project
    target_dir.mkdir(parents=True, exist_ok=True)
    current = active(target_dir)
    if current:
        raise SystemExit(f"active implementation slot occupied: {current[0]}")
    target = target_dir / source.name
    shutil.copy2(source, target)
    print(target.relative_to(Path.cwd()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
