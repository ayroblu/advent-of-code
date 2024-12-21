from collections import defaultdict

from utils.file import read_input

contents = read_input(__file__)

options, pats = contents.split("\n\n")
options = options.split(", ")
pats = pats.splitlines()


def check_possible(remaining: str, possibles: defaultdict[str, int]) -> int:
    if remaining in possibles:
        return possibles[remaining]

    sub_possible = 0
    for option in options:
        if remaining.startswith(option):
            if len(remaining) == len(option):
                sub_possible += 1
            sub_possible += check_possible(remaining[len(option) :], possibles)
    possibles[remaining] = sub_possible
    return sub_possible


possible = 0

for pat in pats:
    possible += check_possible(pat, defaultdict(int))

print(possible)
