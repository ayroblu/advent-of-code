from itertools import batched

from utils.file import read_input

contents = read_input(__file__)

sum = 0
for group in batched(contents.splitlines(), 3):
    data = [set(g) for g in group]
    same: set[str] = set.intersection(*data)  # type: ignore
    letter = same.pop()
    s = ord(letter)
    if s >= ord("a"):
        res = s - ord("a") + 1
    else:
        res = s - ord("A") + 27
    sum += res

print(sum)
