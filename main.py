#!/usr/bin/env python3
"""Write one crypto trading joke to /output/entry.txt."""

import os

JOKE = "My trading group only wakes up when someone loses money. We had 400 messages yesterday. I was the main character."

def main():
    assert 1 <= len(JOKE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in JOKE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
