#!/usr/bin/env python3
"""Deadpan forecast for a city that does not exist.

Writes one forecast line (at most 160 characters, one line, no
trailing newline) to /output/entry.txt for the make.fun bounty
"Deadpan Forecasts for Cities That Do Not Exist".

The line is fixed text: no clock, no randomness, no network, so
every run produces byte-identical output. The file is created
world-readable (mode 0644); the output directory itself is never
chmodded.
"""

import os
import sys

# Final forecast line (v2): the draft underused the 160 characters
# (judge criterion 5), so the same missing-mountain premise gets its
# third beat -- a visibility figure -- keeping one coherent joke,
# a broadcast structure (fog / highs / lows / visibility) and three
# concrete numbers (9am, 14, 10 km).
FORECAST = (
    "In Brume, fog will lift by 9am, revealing the mountain was never "
    "there. Highs of 14, lows of mild regret, visibility improving "
    "to 10 km of nothing."
)


def output_path() -> str:
    """Where the entry text goes: the harness dir if set, else /output."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(base, "entry.txt")


def main() -> int:
    path = output_path()
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
    except OSError:
        pass
    data = FORECAST.encode("utf-8")
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    try:
        os.write(fd, data)
    finally:
        os.close(fd)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
