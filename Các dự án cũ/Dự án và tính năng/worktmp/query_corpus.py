from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("corpus", type=Path)
    parser.add_argument("pattern")
    parser.add_argument("--context", type=int, default=800)
    parser.add_argument("--max", type=int, default=30)
    args = parser.parse_args()

    records = json.loads(args.corpus.read_text(encoding="utf-8"))
    regex = re.compile(args.pattern, re.IGNORECASE | re.MULTILINE)
    hits = 0
    for record in records:
        text = record.get("text", "")
        for match in regex.finditer(text):
            hits += 1
            start = max(0, match.start() - args.context)
            end = min(len(text), match.end() + args.context)
            print(f"\n===== {record['relative_path']} | hit {hits} | {match.group(0)!r} =====")
            print(text[start:end])
            if hits >= args.max:
                return


if __name__ == "__main__":
    main()
