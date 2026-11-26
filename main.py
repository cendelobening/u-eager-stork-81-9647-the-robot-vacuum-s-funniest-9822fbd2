#!/usr/bin/env python3
"""The Robot Vacuum's Funniest Excuse.

Writes a single line (at most 120 characters) in which a robot vacuum
explains why it missed a spot, to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output/entry.txt when the variable is unset).

Pure Python standard library only; no third-party packages.
"""

import os

LINE = "My brush roll filed for workers' comp after one look at that pet hair, so I'm on light duty now."


def main():
    # Gate: one line, 1-120 characters, not only whitespace.
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    if not 1 <= len(LINE) <= 120:
        raise ValueError("entry must be 1-120 characters, got %d" % len(LINE))
    if not LINE.strip():
        raise ValueError("entry must not be only whitespace")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    try:
        os.write(fd, data)
        # os.open's mode is masked by the umask; force 0644 so the
        # grader can always read the file.
        os.fchmod(fd, 0o644)
    finally:
        os.close(fd)


if __name__ == "__main__":
    main()
