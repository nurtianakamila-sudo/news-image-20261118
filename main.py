#!/usr/bin/env python3
"""news-image-20261118 v2 entrypoint.

Copies the bundled front-page image (entry.png, in this repository) to
the output directory and verifies the copy byte for byte.

The output directory comes from MAKEFUN_OUTPUT_DIR and defaults to
/output. The program uses only the Python standard library and needs
no network.
"""

import hashlib
import os
import shutil
import sys

IMAGE_NAME = "entry.png"


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, IMAGE_NAME)
    # The grader runs the program with MAKEFUN_OUTPUT_DIR set; the
    # default /output matches the competition's stated output path.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(out_dir, IMAGE_NAME)

    if not os.path.isfile(source):
        print(f"error: bundled image not found: {source}", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(source, target)

    want = sha256_of(source)
    got = sha256_of(target)
    if want != got:
        print(
            f"error: copy mismatch for {target}: "
            f"expected sha256 {want}, got {got}",
            file=sys.stderr,
        )
        return 1

    print(f"wrote {target} (sha256 {got})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
