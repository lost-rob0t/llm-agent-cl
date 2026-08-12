#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FRONT = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def main() -> int:
    manifest_path = ROOT / "skills" / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    errors: list[str] = []
    skills = manifest.get("skills", [])
    if manifest.get("skill_count") != len(skills):
        errors.append("manifest skill_count does not match skills length")
    names: set[str] = set()
    for item in skills:
        name = item.get("name")
        path = ROOT / item.get("path", "")
        if name in names:
            errors.append(f"duplicate skill name: {name}")
        names.add(name)
        if not path.is_file():
            errors.append(f"missing skill file: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        if not FRONT.search(text):
            errors.append(f"missing YAML frontmatter: {path.relative_to(ROOT)}")
        if f'name: "{name}"' not in text:
            errors.append(f"skill name mismatch: {path.relative_to(ROOT)}")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"validated {len(skills)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
