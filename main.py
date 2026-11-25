"""Write the Midnight Fridge Roast entry to /output/entry.txt.

The line is written exactly, with no trailing newline.
"""

from pathlib import Path


# This is the single submitted roast line.
ENTRY_LINE = "It won't open till six because it knows what I did to the leftover ribs at one a.m. last time."


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY_LINE, encoding="utf-8")
    print(ENTRY_LINE)


if __name__ == "__main__":
    main()
