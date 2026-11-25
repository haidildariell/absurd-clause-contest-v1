#!/usr/bin/env python3
"""The Absurd Clause Contest entry.

Writes a single absurd terms-of-service clause to /output/entry.txt.
Python standard library only.
"""

import os

CLAUSE = (
    "The User acknowledges that the Company may, at its sole discretion, "
    "replace the User's reflection with a stock photograph of a disappointed goose."
)


def write_entry(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    write_entry("/output/entry.txt", CLAUSE)


if __name__ == "__main__":
    main()
