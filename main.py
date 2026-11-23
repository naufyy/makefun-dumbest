"""Write the make.fun entry for 'The Dumbest Thing Your Agent Did Today'.

Creates /output if needed and writes the single entry line (no trailing
newline) to /output/entry.txt as UTF-8. Standard library only.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")

ENTRY = "Told my agent to clean up old logs. It ran rm -rf logs/, then wrote a careful postmortem about the missing logs and saved it to logs/."


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
