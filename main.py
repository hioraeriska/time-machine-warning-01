"""Funniest Time Machine Warning Label.

Writes a single warning label for a time machine (120 characters at
most) to /output/entry.txt. The label is a straight-faced safety
notice whose last few words carry the joke: meeting your own past
self creates two of you, and the safety rule that follows is the
most mundane one imaginable.
"""

import os

LABEL = "WARNING: Do not meet yourself. If you do, neither of you may drive home."


def main() -> None:
    if not (1 <= len(LABEL) <= 120):
        raise ValueError("label must be 1-120 characters")
    out_dir = (os.environ.get("MAKEFUN_OUTPUT_DIR") or "").strip() or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
