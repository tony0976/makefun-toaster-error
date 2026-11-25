#!/usr/bin/env python3
"""Writes this entry's text to /output/entry.txt."""

import os

# Deadpan appliance voice: a real-looking error code, then the toaster gives up on breakfast entirely.
TEXT = """ERROR 404: BREAD NOT FOUND. Insert bread, or accept that breakfast has officially left the chat."""

MAX_CHARS = 120

def main():
    # The bounty scores one toaster error line of at most 120 chars; fail loudly instead of submitting a malformed entry.
    assert 1 <= len(TEXT) <= MAX_CHARS, f"entry must be 1-{MAX_CHARS} chars, got {len(TEXT)}"
    assert "\n" not in TEXT, "entry must be a single line"
    assert TEXT.startswith("ERROR"), "entry must read like a real appliance error message"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote {len(TEXT)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()
