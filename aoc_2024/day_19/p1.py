from utils.file import read_input

contents = read_input(__file__)

options, pats = contents.split("\n\n")
options = options.split(", ")
pats = pats.splitlines()


def check_possible(remaining: str, seen: set[str]) -> bool:
    if remaining in seen:
        return False
    seen.add(remaining)

    for option in options:
        if remaining.startswith(option):
            if len(remaining) == len(option):
                return True
            if check_possible(remaining[len(option) :], seen):
                return True
    return False


possible = 0

for pat in pats:
    if check_possible(pat, set()):
        possible += 1

print(possible)
