from utils.file import read_input

contents = read_input(__file__)

# contents = """#.#####################
##.......#########...###
########.#########.#.###
####.....#.>.>.###.#.###
####v#####.#v#.###.#.###
####.>...#.#.#.....#...#
####v###.#.#.#########.#
####...#.#.#.......#...#
######.#.#.#######.#.###
##.....#.#.#.......#...#
##.#####.#.#.#########v#
##.#...#...#...###...>.#
##.#.#v#######v###.###v#
##...#.>.#...>.>.#.###.#
######v#.#.###v#.#.###.#
##.....#...#...#.#.#...#
##.#########.###.#.#.###
##...###...#...#...#.###
####.###.#.###v#####v###
##...#...#.#.>.>.#.>.###
##.###.###.#.###.#.#v###
##.....###...###...#...#
######################.#"""

grid = [line for line in contents.splitlines()]
rs, cs = (0, 0)
for c, char in enumerate(grid[0]):
    if char == ".":
        cs = c
        break

dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
slips = ">v^<"

type Point = tuple[int, int]
paths: list[tuple[Point, int, set[Point]]] = [((rs, cs), 0, set())]
seen: set[Point] = set()
max_dist = 0
while len(paths) > 0:
    next_paths: list[tuple[Point, int, set[Point]]] = []
    for (r, c), dist, seen in paths:
        for rd, cd in dirs:
            if grid[r][c] in slips:
                force_dir = dirs[slips.index(grid[r][c])]
                if (rd, cd) != force_dir:
                    continue
            nr, nc = next_point = (r + rd, c + cd)
            new_dist = dist + 1
            if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
                continue
            if next_point in seen:
                continue
            seen = seen.copy()
            seen.add(next_point)
            if grid[nr][nc] == "#":
                continue
            max_dist = max(max_dist, new_dist)
            next_paths.append(((nr, nc), new_dist, seen))

    paths = next_paths

print(max_dist)
