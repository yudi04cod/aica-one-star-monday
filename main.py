#!/usr/bin/env python3
"""One Star for Monday — make.fun entry.

Writes a single line to /output/entry.txt: a one-star review of Monday
written as though Monday were a restaurant. Python 3.13 standard library
only; no input, no network, deterministic output.
"""

import os

LINE = (
    "One star. The server brought the wrong week, the food was cold, "
    "and the bill cost my whole weekend."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
