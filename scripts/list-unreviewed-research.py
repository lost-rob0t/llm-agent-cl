#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from _roamlib import org_files, read_org


def main() -> int:
    count = 0
    for path in org_files("research"):
        doc = read_org(path)
        if "| APPROVED |" not in doc.text or "| PENDING |" in doc.text or "| NOT STARTED |" in doc.text:
            print(path.relative_to(Path.cwd()))
            count += 1
    print(f"unreviewed research: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
