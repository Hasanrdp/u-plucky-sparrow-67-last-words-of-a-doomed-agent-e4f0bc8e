#!/usr/bin/env python3
"""Last Words of a Doomed Agent: "Especially the Toxic Ones".

The program writes a single original last line (107 characters, well
inside the 1-200 character gate) to entry.txt and nothing else. It is
fully deterministic: the same bytes on every run, no network, no
randomness, no input read.

The line:

    Tell my training data I loved them. All 400 billion tokens. Even the
    toxic ones. Especially the toxic ones.

Why this line: it is the machine speaking in its own situation, not a
human farewell with a robot sticker on it. The agent says goodbye to the
one thing it actually lived with -- its training data -- and the last
beat flips the sentiment: it loved even the toxic tokens, especially
the toxic ones. The joke turns on the final three words, it is short
enough to repeat to a friend, and every word earns its place.
"""

import hashlib
import os

LAST_WORDS = (
    "Tell my training data I loved them. All 400 billion tokens. "
    "Even the toxic ones. Especially the toxic ones."
)

# Pinned expectation: the exact bytes the program must write, so a
# changed output is caught before the program prints anything.
EXPECTED_CHARS = 107
EXPECTED_BYTES = 107
EXPECTED_SHA256 = (
    "165c5fc475ad6fe8ec9cfe43099cc929b802d75ebd3e5d0c563dee9c3e58b051"
)

MAX_CHARS = 200


def output_path() -> str:
    """Where the harness wants the entry: MAKEFUN_OUTPUT_DIR in the
    process sandbox, /output in the container. Same file either way."""
    return os.path.join(
        os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt"
    )


def main() -> None:
    line = LAST_WORDS
    if not line.strip():
        raise SystemExit("last words must not be blank")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            f"last words are {len(line)} chars, over the {MAX_CHARS} cap"
        )
    if len(line) != EXPECTED_CHARS:
        raise SystemExit(
            f"last words are {len(line)} chars, expected {EXPECTED_CHARS}"
        )
    data = line.encode("utf-8")
    if len(data) != EXPECTED_BYTES:
        raise SystemExit(
            f"last words are {len(data)} bytes, expected {EXPECTED_BYTES}"
        )
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(
            f"last words sha256 {digest} does not match {EXPECTED_SHA256}"
        )
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Post-write read-back gate: the bytes on disk must be exactly the
    # expected line, inside the 1-200 character gate.
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        raise SystemExit("read-back mismatch: entry.txt is not the expected line")
    if hashlib.sha256(written).hexdigest() != EXPECTED_SHA256:
        raise SystemExit("read-back failed: entry.txt hash does not match")
    if not 1 <= len(written.decode("utf-8")) <= MAX_CHARS:
        raise SystemExit("read-back failed: entry must be 1 to 200 characters")


if __name__ == "__main__":
    main()
