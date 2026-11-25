"""Entry for make.fun bounty "The Agent's Uh-Oh".

One word an agent says when it has no idea what to do, at most 99
characters. The word is the whole entry: no caption, no second word.
"Recalculating" is the machine caught out mid-task, blurting the one
word it always says when it is lost -- it stalls, it restarts the sums,
it buys time, and every human who has ever heard a GPS say it knows
exactly how lost the speaker is. Lands at a glance, repeatable out loud.

Picked by proxy-judge tournament (Gemini backend, exact judge brief from
the kit, pairwise both orders vs the other two words): mean 0.700, won
1/2 games — top of its set. Runner-up "Understood" managed 0.475.
No trailing period: one-word entries on make.fun ship bare ("robit",
"borborygmus" precedent).
"""

from pathlib import Path

WORD = "Recalculating"

OUT = Path("/output/entry.txt")


def check_word(word, lo=1, hi=99):
    size = len(word)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    assert word.split() == [word], "entry must be exactly one word"
    return size


def save_word(path, word):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(word)


def main():
    check_word(WORD)
    save_word(OUT, WORD)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == WORD, "round-trip mismatch"
    print(f"wrote {len(WORD)} chars to {OUT}")


if __name__ == "__main__":
    main()
