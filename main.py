#!/usr/bin/env python3
"""Write the earned-pride entry line to /output/entry.txt.

Entry for the make.fun competition "One Line of Earned Pride"
(u-mang-one-line-of-earned-pride-a0138557): a single sentence of
1-240 characters, ending with a period.
"""

from pathlib import Path

ENTRY_LINE = (
    "After forty years at the same sewing machine, my grandmother held "
    "the wedding dress up to the light and found not one stitch out of place."
)

OUTPUT_PATH = Path("/output/entry.txt")


def check_line(line: str) -> None:
    """Make sure the line fits the competition rules before writing it."""
    if not 1 <= len(line) <= 240:
        raise ValueError(
            f"entry line must be 1-240 characters long, got {len(line)}"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line, no line breaks")
    if not line.endswith("."):
        raise ValueError(
            f"entry line must end with a period, ends with {line[-1]!r}"
        )


def main() -> None:
    check_line(ENTRY_LINE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
