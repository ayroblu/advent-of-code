from utils.file import read_input

contents = read_input(__file__)
dist = 26501365

grid = [line for line in contents.splitlines()]

start = (-1, -1)
for r, line in enumerate(grid):
    for c, item in enumerate(line):
        if item == "S":
            start = (r, c)
            break

type Point = tuple[int, int]
dirs: list[Point] = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def fill(start: Point, start_step: int = 1) -> int:
    positions = [start]
    seen: set[Point] = set()
    counter = 0

    for i in range(start_step, dist + 1):
        new_positions: list[Point] = []
        is_countable = (dist - i) % 2 == 0
        for r, c in positions:
            for rd, cd in dirs:
                nr, nc = new_pos = (r + rd, c + cd)
                if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
                    continue
                if grid[nr][nc] == "#":
                    continue
                if new_pos in seen:
                    continue
                seen.add(new_pos)

                new_positions.append(new_pos)
                if is_countable:
                    counter += 1
        positions = new_positions
        if len(new_positions) == 0:
            break
    return counter


counter = fill(start)
# 131 - 65 = next grid, then 131
# 66
# total one_dir = dist // 131
# = 202300.496
# remainder = dist % 131
# = 65
# total_filled_grids = (dist // 131) ** 2
# 4 nsew
# diagonal ones = (total_one_dir - 1) * 4
# start_steps = 131 * total_one_dir
assert len(grid) == len(grid[0])
w = len(grid)
total_one_dir = dist // w
remainder = dist % w
sr, sc = start
end_dist = total_one_dir * w - (w // 2) + 1
top_grid = fill((w - 1, sc), end_dist)
bottom_grid = fill((0, sc), end_dist)
left_grid = fill((sr, w - 1), end_dist)
right_grid = fill((sr, 0), end_dist)

# +1 for over the grid line, +1 for fill starts on the next op
diag_dist = total_one_dir * w + 2
top_left_small = fill((w - 1, w - 1), diag_dist)
top_right_small = fill((w - 1, 0), diag_dist)
bottom_left_small = fill((0, w - 1), diag_dist)
bottom_right_small = fill((0, 0), diag_dist)
total_diag = (
    top_left_small + top_right_small + bottom_left_small + bottom_right_small
) * (total_one_dir)

diag_dist = (total_one_dir - 1) * w + 2
top_left_large = fill((w - 1, w - 1), diag_dist)
top_right_large = fill((w - 1, 0), diag_dist)
bottom_left_large = fill((0, w - 1), diag_dist)
bottom_right_large = fill((0, 0), diag_dist)
total_diag += (
    top_left_large + top_right_large + bottom_left_large + bottom_right_large
) * (total_one_dir - 1)

start_total = fill(start)
start_total_even = fill(start, 2)
total_filled_grids = (
    total_one_dir**2 * start_total_even + (total_one_dir - 1) ** 2 * start_total
)
total = (
    total_filled_grids + top_grid + bottom_grid + left_grid + right_grid + total_diag
)

print(total)
