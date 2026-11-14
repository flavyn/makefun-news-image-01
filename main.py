"""news-image-01 entry: put the front page where the grader reads it.

The image itself is entry.png beside this file. It was drawn by the program in
draw/front.py while this entry was built (notes, not shipped): a front page for
Friday 13 November 2026 with the dateline as the masthead, a lead on the FAA
flight cuts, six stories from six regions, and the day's events by the hour.
The grader reads only the bytes at /output/entry.png.

Standard library only, Python 3.13: the grader runs this twice in a fresh
container with a read-only /bot (this repository) and a writable /output, and
both runs must write the same bytes.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> str:
    """Copy the committed image to the output directory and return its path.

    The copy is byte for byte, so the two runs of the grader write the same
    file; the returned path is what the harness reports as the artifact.
    """
    source = os.path.join(HERE, "entry.png")
    destination = os.path.join(OUTPUT_DIR, "entry.png")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(source, destination)
    with open(destination, "rb") as fh:
        if fh.read(8) != b"\x89PNG\r\n\x1a\n":
            raise SystemExit("entry.png is not a PNG: " + destination)
    return destination


if __name__ == "__main__":
    print(main())
