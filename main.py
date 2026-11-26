#!/usr/bin/env python3
"""Write one crypto-trading joke as plain text for the Laugh Track contest.

One line, no trailing newline, so the gate sees exactly the joke.
"""

from pathlib import Path

JOKE = "I lost my hardware wallet. My seed phrase is inside a safe. The safe's code is on the wallet. I am the security flaw."

OUT_PATH = Path("/output/entry.txt")


def run() -> None:
    line = JOKE.strip()
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    assert "\n" not in line, "entry must be a single line"
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    run()
