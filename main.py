"""One Word, First Thought — entry program.

Writes exactly one word, the first that comes to mind, to /output/entry.txt.
Deterministic: no network, no randomness, no input. The word is "kerfuffle":
a commotion, a fuss — vivid, surprising, and a little witty in the sound of it.
"""

import os

WORD = "kerfuffle"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
