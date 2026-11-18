#!/usr/bin/env python3
"""news-image-20261117 — "Sum up 17 November's world news in one image."

The entry is a single front-page collage, image.png, drawn as vector
artwork (see artwork.svg) and rendered to a 1024x1024 PNG. The program
runs offline in the grader's sandbox and simply copies that image to
the required output path, so both grading runs write identical bytes.

Outside the sandbox, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE_IMAGE = HERE / "image.png"


def output_path() -> Path:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / "entry.png"


def main() -> None:
    target = output_path()
    shutil.copyfile(SOURCE_IMAGE, target)
    written = target.stat().st_size
    expected = SOURCE_IMAGE.stat().st_size
    if written != expected:
        raise SystemExit(f"copy mismatch: wrote {written} of {expected} bytes")
    print(f"wrote {target} ({written} bytes)")


if __name__ == "__main__":
    main()
