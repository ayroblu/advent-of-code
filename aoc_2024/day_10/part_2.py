import numpy as np
from utils.file import read_input

contents = read_input(__file__).strip()
lines = contents.splitlines()
grid = [[int(item) for item in line] for line in lines]

possible = [
    (r, c) for r, row in enumerate(grid) for c, item in enumerate(row) if item == 0
]

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def traverse(pos: tuple[int, int]) -> int:
    r, c = pos
    value = grid[r][c]
    if value == 9:
        return 1
    result = 0
    for dr, dc in dirs:
        r1, c1 = np.add((r, c), (dr, dc))
        if 0 <= r1 < len(grid) and 0 <= c1 < len(grid[0]) and grid[r1][c1] == value + 1:
            result += traverse((r1, c1))
    return result


total = 0
for r, c in possible:
    total += traverse((r, c))

print(total)
