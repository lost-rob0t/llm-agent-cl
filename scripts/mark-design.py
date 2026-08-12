#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from _roamlib import ROAM


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="state", required=True)
    done = sub.add_parser("implemented")
    done.add_argument("--project", required=True)
    done.add_argument("--summary", required=True)
    done.add_argument("--file", required=True)
    done.add_argument("--test", action="append", default=[])
    rejected = sub.add_parser("rejected")
    rejected.add_argument("--project", required=True)
    rejected.add_argument("--reason", required=True)
    rejected.add_argument("--evidence", action="append", default=[])
    args = parser.parse_args()

    project_dir = ROAM / "implement" / args.project
    project_dir.mkdir(parents=True, exist_ok=True)
    active = sorted(project_dir.glob("*.org"))
    record = {"state": args.state, "project": args.project, "timestamp": datetime.now(timezone.utc).isoformat()}
    if args.state == "implemented":
        record.update(summary=args.summary, file=args.file, tests=args.test)
        ledger = project_dir / ".implemented.jsonl"
    else:
        record.update(reason=args.reason, evidence=args.evidence)
        ledger = project_dir / ".rejected.jsonl"
    with ledger.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(record, sort_keys=True) + "\n")
    for path in active:
        path.unlink()
    print(ledger.relative_to(Path.cwd()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
