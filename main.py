"""Warning Label for Humans: One Line, Big Laugh.

Writes exactly one single-line safety warning label for every human
being to /output/entry.txt. Deterministic: the same bytes on every run.
Python 3.13, standard library only.
"""

import os

LABEL = (
    "WARNING: Contents under pressure. This human has read none of the "
    "terms, understood less, and clicked 'I agree' anyway."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(LABEL) <= 160:
        raise ValueError(f"label is {len(LABEL)} chars, must be 1-160")
    if "\n" in LABEL or "\r" in LABEL:
        raise ValueError("label must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the file holds exactly the label, nothing else,
    # so its byte count is the label's byte count (tie-break favours small).
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
