from utils.file import read_input

contents = read_input(__file__)
dist = 64

# contents = """...........
# .....###.#.
# .###.##..#.
# ..#.#...#..
# ....#.#....
# .##..S####.
# .##..#...#.
# .......##..
# .##.#.####.
# .##..##.##.
# ..........."""
# dist = 6

grid = [line for line in contents.splitlines()]

start = (-1, -1)
for r, line in enumerate(grid):
    for c, item in enumerate(line):
        if item == "S":
            start = (r, c)
            break

type Point = tuple[int, int]
dirs: list[Point] = [(1, 0), (0, 1), (-1, 0), (0, -1)]

positions = [start]
grid_dist: dict[Point, int] = {start: 0}
for i in range(dist):
    new_positions: list[Point] = []
    for r, c in positions:
        for rd, cd in dirs:
            nr, nc = new_pos = (r + rd, c + cd)
            if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
                continue
            if grid[nr][nc] == "#":
                continue
            if new_pos in grid_dist:
                continue
            new_positions.append((nr, nc))
            grid_dist[(nr, nc)] = i + 1
    positions = new_positions

counter = 0
for k, v in grid_dist.items():
    if (dist - v) % 2 == 0:
        counter += 1

print(counter)
