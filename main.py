#!/usr/bin/env python3
"""One-line roast entry for make.fun.

Writes a single original roast line about a gadget used every day
to /output/entry.txt. Deterministic: the same line every run.
"""

import os
import sys

LINE = "My smartwatch buzzes to celebrate my 10,000 steps, all of which were me pacing to the fridge."

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> str:
    """Return the line if it is a valid single-line roast, else raise."""
    if not line or not line.strip():
        raise ValueError("roast line must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("roast line must be a single line")
    if len(line) > 200:
        raise ValueError("roast line exceeds 200 characters")
    return line


def main() -> int:
    try:
        line = validate(LINE)
    except ValueError as exc:
        print(f"invalid roast line: {exc}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
