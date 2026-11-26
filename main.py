"""The robot vacuum's funniest excuse for missing a spot.

The joke: the missed spot is not laziness or a dead battery, it is
bureaucracy. The dust in one corner has unionized, elected a
spokesperson, and now the vacuum — a dutiful little machine that
follows rules — needs a permit to enter. The humor comes from the
escalation (dust -> union -> spokesperson -> permit) and from the
vacuum sounding like a defensive employee hiding behind procedure
instead of admitting it just did not clean there. The line is 92
characters, well under the 120-character limit, and it is written in
one breath so it reads like a single flustered excuse blurted out
before the owner can ask a follow-up question.
"""

import os

LINE = "The dust in that corner unionized, elected a spokesperson, and now I need a permit to enter."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(LINE.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
