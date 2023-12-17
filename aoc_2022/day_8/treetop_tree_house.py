from typing import Iterable

from utils.file import read_input

contents = read_input(__file__)

grid = [[int(c) for c in line] for line in contents.splitlines()]

v_grid = [[False for _ in line] for line in grid]


def map_visible(iterable: Iterable[tuple[int, int]]):
    max_height = -1
    for r, c in iterable:
        v_grid[r][c] = v_grid[r][c] or grid[r][c] > max_height
        max_height = max(max_height, grid[r][c])


for c in range(len(grid[0])):
    top_down = [(r, c) for r in range(len(grid))]
    map_visible(top_down)
    last_r = len(grid) - 1
    bottom_up = [(last_r - r, c) for r in range(len(grid))]
    map_visible(bottom_up)

for r in range(len(grid)):
    left_right = [(r, c) for c in range(len(grid[0]))]
    map_visible(left_right)
    last_c = len(grid[0]) - 1
    right_left = [(r, last_c - c) for c in range(len(grid[0]))]
    map_visible(right_left)

result = sum(item for line in v_grid for item in line)
print(result)
