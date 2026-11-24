#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — the whole entry is a single emoji.

Writes exactly one emoji (1-8 chars, UTF-8) to /output/entry.txt.

The emoji: 🌋 Volcano. A volcano at first light, lava glowing against
dark rock — the trip you brag about forever. Not a beach like everyone
else's postcard: a place with fire in it, a dawn you have to climb for,
a story no one else at the table has.
"""

import os

# --- the emoji -----------------------------------------------------------
EMOJI = "🌋"

MAX_CHARS = 8


def entry_text():
    """Return the single emoji that is the dream vacation."""
    return EMOJI


def run_checks():
    """Self-test the entry the way the sealed scorer gates it."""
    text = entry_text()
    validate(text)
    assert len(text) == 1, "expected 1 char, got %d" % len(text)
    assert text == "🌋", "the emoji drifted: %r" % text
    assert text.encode("utf-8") == b"\xf0\x9f\x8c\x8b", "bytes must be U+1F30B"
    return True


def validate(text):
    """The sealed scorer's gate: 1-8 chars, UTF-8, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-%d chars, got %d" % (MAX_CHARS, len(text)))
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    text.encode("utf-8")
    return True


def main():
    text = entry_text()
    validate(text)
    run_checks()
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
