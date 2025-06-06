from collections import defaultdict

from utils.file import read_input

contents = read_input(__file__)
lines = contents.strip().splitlines()

ant = defaultdict[str, list[tuple[int, int]]](list)
for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if char != ".":
            ant[char].append((r, c))

rl = len(lines)
cl = len(lines[0])

antinodes = set[tuple[int, int]]()
for ants in ant.values():
    for i, (ar, ac) in enumerate(ants[:-1]):
        for br, bc in ants[(i + 1) :]:
            dr, dc = (ar - br, ac - bc)
            r1, c1 = (ar + dr, ac + dc)
            r2, c2 = (br - dr, bc - dc)
            if 0 <= r1 < rl and 0 <= c1 < cl:
                antinodes.add((r1, c1))
            if 0 <= r2 < rl and 0 <= c2 < cl:
                antinodes.add((r2, c2))

print(len(antinodes))
