from utils.file import read_input

contents = read_input(__file__)

grid = [[ord(ch) for ch in line] for line in contents.splitlines()]

type Point = tuple[int, int]
start: Point = (-1, -1)
end: Point = (-1, -1)
for r, line in enumerate(grid):
    for c, ch in enumerate(line):
        if ch == ord("S"):
            start = (r, c)
            line[c] = ord("a")
        if ch == ord("E"):
            end = (r, c)
            line[c] = ord("z")

seen: set[Point] = set([start])

points = [start]


def run() -> int:
    counter = 0
    global points
    while len(points):
        counter += 1
        new_points: list[Point] = []
        for r, c in points:
            for rd, cd in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr, nc = (r + rd, c + cd)
                if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
                    continue
                if grid[nr][nc] > grid[r][c] + 1:
                    continue
                if (nr, nc) == end:
                    return counter
                if (nr, nc) in seen:
                    continue
                seen.add((nr, nc))
                new_points.append((nr, nc))
        points = new_points
    raise Exception("failed")


print(run())
