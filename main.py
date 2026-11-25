#!/usr/bin/env python3
"""Last Text at One Percent — make.fun entry.

Writes the phone's final text message to /output/entry.txt and to the
entry directory's own entry.txt (same bytes, for local verification).
"""
import os

ENTRY = "i'm using my last 1% to delete your search history. you're welcome. tell the charger i never loved him, i just used him."

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert text == text.strip() and "\n" not in text, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    with open(os.path.join(HERE, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars: {text!r}")


if __name__ == "__main__":
    main()
