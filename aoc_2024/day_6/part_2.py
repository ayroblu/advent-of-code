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
rotation_mat = [[0, 1], [-1, 0]]


def check_loop(custom: tuple[int, int]):
    dr: int = -1
    dc: int = 0

    r, c = init_pos
    seen = set[tuple[tuple[int, int], tuple[int, int]]]()
    seen.add((init_pos, (dr, dc)))

    is_loop = False
    while True:
        nr = r + dr
        nc = c + dc
        if not (0 <= nr < len(lines) and 0 <= nc < len(lines[0])):
            break
        if lines[nr][nc] == "#" or (nr, nc) == custom:
            dr, dc = np.matmul(rotation_mat, (dr, dc))
            continue
        r = nr
        c = nc
        new_item = ((r, c), (dr, dc))
        if new_item in seen:
            is_loop = True
            break
        seen.add(new_item)
    return is_loop


count = 0
for r, line in enumerate(lines):
    print(r)
    for c, char in enumerate(line):
        if char != "^" and char != "#" and check_loop((r, c)):
            count += 1

print(count)
