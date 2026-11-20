"""news-image-20261119 entry: write the day's news image to /output/entry.png.

The image (entry.png, beside this file) is a newspaper-style front page
summing up the world news of Thursday 19 November 2026: the Trump-Xi-Putin
Shenzhen summit, the ICJ's Myanmar genocide ruling, the Gaza raid, the
Hormuz tanker attacks, the Kerch Bridge strike, Anthropic's IPO, Voyager 1
reaching one light-day, and the Senegal boat disaster.

The grader runs this program with no network and a read-only repository,
so the program only copies the shipped image to the output path. It uses
nothing but the Python standard library, and it is deterministic: every
run writes exactly the same bytes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"image missing from repository: {SOURCE}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    # The gate reads exactly these bytes, so fail loudly if the copy
    # somehow differs from the shipped image instead of entering a
    # corrupted file.
    if target.read_bytes() != SOURCE.read_bytes():
        raise SystemExit("copied image does not match the shipped entry.png")


if __name__ == "__main__":
    main()
