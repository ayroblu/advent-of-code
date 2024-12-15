from utils.file import read_input

contents = read_input(__file__).strip()

puzzle, actions = contents.split("\n\n")
doubling = {
    "#": "##",
    "O": "[]",
    ".": "..",
    "@": "@.",
}
grid = [[c for part in line for c in doubling[part]] for line in puzzle.splitlines()]
actions = "".join(actions.splitlines())

start = (0, 0)
for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char == "@":
            start = (r, c)


def push(pos: tuple[int, int], dir: tuple[int, int]) -> bool:
    dr, dc = dir
    r1, c1 = pos
    frontier = [(r1, c1)]
    dcO = 1 if grid[r1][c1] == "[" else -1
    frontier.append((r1, c1 + dcO))
    tomove = frontier
    seen = set(tomove)

    while len(frontier) > 0:
        newfrontier = list[tuple[int, int]]()
        for rf, cf in frontier:
            rf2, cf2 = rf + dr, cf + dc
            if grid[rf2][cf2] == "#":
                return False
            elif grid[rf2][cf2] in {"[", "]"}:
                if (rf2, cf2) in seen:
                    continue
                seen.add((rf2, cf2))
                newfrontier.append((rf2, cf2))
                dcO = 1 if grid[rf2][cf2] == "[" else -1
                newfrontier.append((rf2, cf2 + dcO))
                seen.add((rf2, cf2 + dcO))
        frontier = newfrontier
        tomove.extend(newfrontier)
    pre = sum("[" == char for line in grid for char in line)
    for rm, cm in reversed(tomove):
        grid[rm + dr][cm + dc] = grid[rm][cm]
        grid[rm][cm] = "."
    post = sum("[" == char for line in grid for char in line)
    if pre != post:
        print("FAIL", pos, dir, tomove)
    return True


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
    elif grid[r1][c1] in {"[", "]"}:
        if dr == 0:
            r2, c2 = (r1, c1)
            while grid[r2][c2] in {"[", "]"}:
                r2, c2 = (r2 + dr, c2 + dc)
            if grid[r2][c2] == "#":
                pass
            else:
                for pc in range(c2, c1, -dc):
                    grid[r1][pc] = grid[r1][pc - dc]
                grid[r1][c1] = "."
                rr, rc = (r1, c1)
        else:
            if push((r1, c1), (dr, dc)):
                rr, rc = (r1, c1)

total = 0
for line in grid:
    print("".join(line))
print(rr, rc)
for r, line in enumerate(grid):
    for c, char in enumerate(line):
        if char == "[":
            total += r * 100 + c

print(total)
