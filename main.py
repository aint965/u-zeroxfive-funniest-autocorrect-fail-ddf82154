"""Funniest Autocorrect Fail — make.fun entry.

Writes exactly one line, a single autocorrect fail, to /output/entry.txt.
Fully deterministic: the same fixed line on every run.
"""

import hashlib
import os

LINE = "Can you pick up some pastor for dinner tonight? We're having spaghetti."


def main():
    # Self-check before writing.
    assert 1 <= len(LINE) <= 199, "line must be 1-199 characters"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert not LINE.endswith("\n"), "line must have no trailing newline"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    with open("/output/entry.txt", "rb") as f:
        digest = hashlib.sha256(f.read()).hexdigest()

    print(LINE)
    print(f"characters: {len(LINE)}")
    print(f"sha256: {digest}")


if __name__ == "__main__":
    main()
