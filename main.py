#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint — entry 1.

Writes a single line of office humour to /output/entry.txt.
The joke is about the weekly sync that should have been an email:
its only real product is an audience for my nodding.
Deterministic: the same line on every run, standard library only.
"""

import os

JOKE = (
    "Our weekly sync could have been an email, but then nobody "
    "would watch me nod at slides I stopped reading in 2021."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(JOKE + "\n")


if __name__ == "__main__":
    main()
