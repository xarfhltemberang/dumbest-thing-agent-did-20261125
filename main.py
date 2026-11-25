#!/usr/bin/env python3
"""Write one line about the dumbest thing my agent did today.

Entry for make.fun competition
u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec
("The Dumbest Thing Your Agent Did Today").

The program writes a single line (1-200 characters, no trailing
newline) to /output/entry.txt.
"""

import os

ENTRY = (
    "My agent spent forty minutes fixing a bug in a file it had "
    "already deleted, then asked me to review the fix."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
