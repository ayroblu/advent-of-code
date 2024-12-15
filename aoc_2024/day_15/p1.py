from utils.file import read_input

contents = read_input(__file__).strip()

puzzle, actions = contents.split("\n\n")
grid = [[c for c in line] for line in puzzle.splitlines()]
actions = "".join(actions.splitlines())

start = (0, 0)
for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char == "@":
            start = (r, c)

dirs = {
    "<": (0, -1),
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
}
rr, rc = start
grid[rr][rc] = "."
for action in actions:
    dr, dc = dirs[action]
    r1, c1 = (rr + dr, rc + dc)
    if grid[r1][c1] == "#":
        pass
    elif grid[r1][c1] == ".":
        # grid[r1][c1] = "@"
        # grid[rr][rc] = "."
        rr, rc = (r1, c1)
    elif grid[r1][c1] == "O":
        r2, c2 = (r1, c1)
        while grid[r2][c2] == "O":
            r2, c2 = (r2 + dr, c2 + dc)
        if grid[r2][c2] == "#":
            pass
        else:
            grid[r1][c1] = "."
            grid[r2][c2] = "O"
            rr, rc = (r1, c1)

total = 0
for r, line in enumerate(grid):
    for c, char in enumerate(line):
        if char == "O":
            total += r * 100 + c

print(total)
