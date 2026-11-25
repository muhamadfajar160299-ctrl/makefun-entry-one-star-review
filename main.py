"""Copy entry.txt to the grader output directory.

Reads the single-line review shipped beside this script and writes it
directly to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when the
variable is unset), with no temporary file and no rename, so the output
keeps mode 0644 and stays readable by the grader.
"""
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.txt"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
OUT = OUT_DIR / "entry.txt"


def main():
    data = SRC.read_bytes()
    try:
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        OUT.write_bytes(data)
        os.chmod(OUT, 0o644)
    except OSError as exc:
        raise SystemExit(f"cannot write output entry: {exc}") from exc


if __name__ == "__main__":
    main()
