from typing import Iterable

from utils.file import read_input

contents = read_input(__file__)

grid = [[int(c) for c in line] for line in contents.splitlines()]


def get_distance(iterable: Iterable[tuple[int, int]], height: int) -> int:
    distance = 0
    for r, c in iterable:
        distance += 1
        if grid[r][c] >= height:
            return distance
    return distance


max_value = 0
for r, line in enumerate(grid):
    for c, item in enumerate(line):
        top = get_distance([(nr, c) for nr in reversed(range(0, r))], item)
        left = get_distance([(r, nc) for nc in reversed(range(0, c))], item)
        right = get_distance([(r, nc) for nc in range(c + 1, len(grid[0]))], item)
        bottom = get_distance([(nr, c) for nr in range(r + 1, len(grid))], item)
        value = top * left * right * bottom
        max_value = max(max_value, value)

print("result", max_value)
