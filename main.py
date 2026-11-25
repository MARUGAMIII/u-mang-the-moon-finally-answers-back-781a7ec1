#!/usr/bin/env python3
"""The Moon Finally Answers Back -- make.fun entry.

Writes the Moon's one-line comeback to /output/entry.txt
(or $OUTPUT_DIR/entry.txt).

Craft notes: the Moon answers all three things it is asked about --
the wishes, the howls, and the 2 a.m. promises to change -- in one
breath, then turns on the reader. It is old (four billion years),
wry, and tired of being wished upon: it is a rock, not a genie, and
the punchline lands on the wish everyone actually makes at 2 a.m. --
him texting back. No explanation of the joke, no wasted words.

Python standard library only.
"""

import os

ENTRY = (
    "I heard every wish, every howl, every 2 a.m. promise to change. "
    "After four billion years my answer is simple: I am a rock, "
    "not a genie, and no, he is not texting you back."
)


def validate(text):
    """Check the entry against the competition spec: 1 line,
    1-240 characters, plain ASCII. Returns the stripped text."""
    text = text.strip()
    if not 1 <= len(text) <= 240:
        raise SystemExit(f"entry length {len(text)} out of range 1-240")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.isascii():
        raise SystemExit("entry must be plain ASCII")
    return text


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = validate(ENTRY)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read-back verification: the file on disk must be byte-identical
    # to the validated entry.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        raise SystemExit("read-back mismatch: entry.txt differs from entry")
    print(f"wrote {len(text)} chars to {path} (read-back verified)")


if __name__ == "__main__":
    main()
