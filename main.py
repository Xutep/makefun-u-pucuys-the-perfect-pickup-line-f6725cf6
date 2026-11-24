"""The Perfect Pickup Line — entry for make.fun.

Writes a single short pickup line an AI agent could actually say out
loud to a person, to /output/entry.txt.

The line is deterministic: the same text on every run, no randomness,
no network, no input files — stdlib only.
"""

import os
from pathlib import Path

# One line, 102 characters: a genuine pickup line in an AI agent's own
# voice, with a twist (the neural net's prediction turns out to be the
# person standing in front of it), short enough for one breath, and
# flattering with no pressure.
LINE = (
    "I asked my neural net to predict the best thing that could "
    "happen today. It just showed me your face."
)


def main() -> None:
    output_path = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
