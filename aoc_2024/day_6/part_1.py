import numpy as np
from utils.file import read_input

contents = read_input(__file__)
lines = contents.strip().splitlines()

init_pos = None
for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if char == "^":
            init_pos = (r, c)

assert init_pos is not None
dr: int = -1
dc: int = 0

rotation_mat = [[0, 1], [-1, 0]]

r, c = init_pos
count = 1
seen = set[tuple[int, int]]()
seen.add(init_pos)
while True:
    nr = r + dr
    nc = c + dc
    if not (0 <= nr < len(lines) and 0 <= nc < len(lines[0])):
        break
    if lines[nr][nc] == "#":
        dr, dc = np.matmul(rotation_mat, (dr, dc))
        continue
    r = nr
    c = nc
    seen.add((r, c))

print(len(seen))
