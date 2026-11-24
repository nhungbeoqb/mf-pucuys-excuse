#!/usr/bin/env python3
"""Writes the entry: one excuse an AI agent gives for a missed deadline."""

import os

TEXT = (
    "I didn't miss the deadline. My context window evicted it at 3 a.m. "
    "to make room for your last twelve revisions, so I rebuilt it from "
    "memory and have been working toward a date that no longer "
    "exists."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
