"""ai-happy-01 entry: copy the repo's image to the output directory.

The program writes one image, /output/entry.png, for the make.fun
"Make the AI judge happy" bounty. It copies the image the repository
holds (entry.png) to the output directory, unchanged, so both runs of
the program produce byte-identical output.

Usage (outside the grader's container):
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"


def main() -> None:
    if not SOURCE.is_file():
        raise FileNotFoundError(f"entry image missing: {SOURCE}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    if target.resolve() == SOURCE.resolve():
        # Output already is the source file; nothing to copy.
        return
    shutil.copyfile(SOURCE, target)


if __name__ == "__main__":
    main()
