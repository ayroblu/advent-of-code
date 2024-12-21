from collections import defaultdict

from utils.file import read_input

contents = read_input(__file__)
min_check = 100

lines = contents.splitlines()

start = (0, 0)
end = (0, 0)

for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if char == "S":
            start = (r, c)
        elif char == "E":
            end = (r, c)

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

path = [start]
dist = defaultdict[tuple[int, int], int](int)
dist[start] = 0
pos = start
counter = 0
while pos != end:
    counter += 1
    for dr, dc in dirs:
        r, c = pos
        r1, c1 = r + dr, c + dc
        if (r1, c1) in dist:
            continue
        if lines[r1][c1] != "#":
            pos = r1, c1
            path.append((r1, c1))
            dist[r1, c1] = counter
            break
    else:
        assert False

num = 0
for r, c in path:
    seen = set[tuple[int, int]]()
    current = dist[r, c]
    for dr in range(21):
        for dc in range(21 - dr):
            for mx in (1, -1):
                for mc in (1, -1):
                    d = dr + dc
                    r1, c1 = r + dr * mx, c + dc * mc
                    if (r1, c1) in seen:
                        continue
                    seen.add((r1, c1))
                    new = dist[r1, c1]
                    if new > current and new - current >= min_check + d:
                        num += 1

print(num)
