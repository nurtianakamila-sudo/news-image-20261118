"""News-image entry: copy the bundled front-page image to /output/entry.png.

The image (entry.png beside this file) sums up the world's news of
Wednesday 18 November 2026. Standard library only, offline, deterministic:
a byte copy, so two runs always write identical bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"), os.path.join(OUT, "entry.png"))
