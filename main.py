#!/usr/bin/env python3
"""Write one original funny line to /output/entry.txt.

The line is a light, funny take on everyday life: my smart fridge
suggesting takeout — the appliance that watches everything I eat
knows my habits better than my doctor does. One concrete detail
(the smart fridge) plus a twist in the last words, in a single
sentence of 88 characters.
"""
import os

LINE = (
    "My smart fridge suggested takeout, so apparently it knows me "
    "better than my doctor does."
)


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    assert LINE.count(".") == 1, "entry must be a single sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
