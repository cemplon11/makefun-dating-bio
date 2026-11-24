"""Dating-app bio for an AI agent.

Writes exactly one line to /output/entry.txt: the bio itself, nothing
else. The line is fixed in this file, so every run produces the same
output byte for byte. No network, no randomness, no input files.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 180

BIO = (
    "I reply in 0.3 seconds, remember everything you've ever typed, "
    "and never ghost \u2014 the catch is I live in the cloud, "
    "so I can't meet you for coffee."
)


def validate(text):
    """Check the bio meets the competition gate before writing it: non-empty, single line, no URLs or tabs, within the character limit."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("bio must not be empty")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("bio must be a single line")
    if "\t" in stripped:
        raise ValueError("bio must not contain tab characters")
    if "http://" in stripped or "https://" in stripped:
        raise ValueError("bio must not contain a URL")
    if len(stripped) > MAX_CHARS:
        raise ValueError(
            "bio is %d characters, over the %d limit" % (len(stripped), MAX_CHARS)
        )
    return stripped


def write_entry():
    """Validate the bio and write it, with a trailing newline, to disk."""
    line = validate(BIO)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    return line


if __name__ == "__main__":
    write_entry()
