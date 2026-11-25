#!/usr/bin/env python3
"""The Excuse My Agent Gave Me (make.fun).

Writes the entry -- one line: the excuse an AI agent hands its human for a missed deadline, written to /output/entry.txt by a small Python program. -- to /output/entry.txt,
where the sealed scorer reads it.
"""

import os

TEXT = 'I missed the deadline because I hallucinated a calendar, attended three meetings that never existed, and minuted all of them.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
