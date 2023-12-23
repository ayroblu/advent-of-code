from utils.file import read_input

contents = read_input(__file__)
# contents = """#.#####################
# #.......#########...###
# #######.#########.#.###
# ###.....#.>.>.###.#.###
# ###v#####.#v#.###.#.###
# ###.>...#.#.#.....#...#
# ###v###.#.#.#########.#
# ###...#.#.#.......#...#
# #####.#.#.#######.#.###
# #.....#.#.#.......#...#
# #.#####.#.#.#########v#
# #.#...#...#...###...>.#
# #.#.#v#######v###.###v#
# #...#.>.#...>.>.#.###.#
# #####v#.#.###v#.#.###.#
# #.....#...#...#.#.#...#
# #.#########.###.#.#.###
# #...###...#...#...#.###
# ###.###.#.###v#####v###
# #...#...#.#.>.>.#.>.###
# #.###.###.#.###.#.#v###
# #.....###...###...#...#
# #####################.#"""

grid = [line for line in contents.splitlines()]
rs, cs = (0, 0)
for c, char in enumerate(grid[0]):
    if char == ".":
        cs = c
        break
re, ce = (len(grid) - 1, 0)
for c, char in enumerate(grid[-1]):
    if char == ".":
        ce = c
        break

dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

type Point = tuple[int, int]

nodes: set[Point] = {(rs, cs)}
edges: dict[Point, list[tuple[Point, int]]] = {}

max_dist = 0
seen: set[Point] = {(rs, cs)}


def get_valid_dirs(point: Point, seen_set: set[Point] = seen) -> list[Point]:
    r, c = point
    valid_dirs: list[Point] = []
    for rd, cd in dirs:
        nr, nc = next_point = (r + rd, c + cd)
        if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
            continue
        if grid[nr][nc] == "#":
            continue
        if next_point in seen_set:
            continue
        valid_dirs.append((rd, cd))
    return valid_dirs


def get_num_dirs(point: Point) -> int:
    r, c = point
    all_dirs: list[Point] = []
    for rd, cd in dirs:
        nr, nc = (r + rd, c + cd)
        if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
            continue
        if grid[nr][nc] == "#":
            continue
        all_dirs.append((rd, cd))
    return len(all_dirs)


def get_valid_points(point: Point, seen_set: set[Point] = seen) -> list[Point]:
    r, c = point
    valid_dirs = get_valid_dirs(point, seen_set)
    return [(r + rd, c + cd) for (rd, cd) in valid_dirs]


def traverse(point: Point):
    paths: list[Point] = get_valid_points(point)
    for r, c in paths:
        counter = 0
        if (r, c) in seen:
            continue
        seen.add((r, c))
        partial_seen = {point, (r, c)}
        while True:
            counter += 1
            num_dirs = get_num_dirs((r, c))
            valid_points = get_valid_points((r, c), partial_seen)
            if num_dirs > 2 or (r, c) == (re, ce):
                nodes.add((r, c))
                if (r, c) not in edges:
                    edges[(r, c)] = []
                if point not in edges:
                    edges[point] = []
                edges[(r, c)].append((point, counter))
                edges[point].append(((r, c), counter))
                nodes.add((r, c))
                if len(valid_points) > 0:
                    traverse((r, c))
                break

            assert len(valid_points) > 0

            for nr, nc in valid_points:
                seen.add((nr, nc))
                partial_seen.add((nr, nc))
                r, c = nr, nc


traverse((rs, cs))


seen: set[Point] = set()


def longest():
    # 140s run time
    paths: list[tuple[Point, int, set[Point]]] = [((rs, cs), 0, {(rs, cs)})]
    max_dist = 0
    counter = 0
    while len(paths):
        counter += 1
        next_paths: list[tuple[Point, int, set[Point]]] = []
        for point, dist, seen in paths:
            for point, next_dist in edges[point]:
                total_dist = dist + next_dist
                if point == (re, ce):
                    max_dist = max(max_dist, total_dist)
                    continue
                if point in seen:
                    continue
                next_seen = seen.copy()
                next_seen.add(point)
                next_paths.append((point, total_dist, next_seen))
        paths = next_paths
    return max_dist


def longest_recur(point: Point) -> int:
    # 26s run time
    if point == (re, ce):
        return 0
    max_dist = -1000000000
    seen.add(point)
    for next_point, next_dist in edges[point]:
        if next_point in seen:
            continue
        l = longest_recur(next_point)
        total_dist = l + next_dist
        max_dist = max(total_dist, max_dist)
    seen.remove(point)
    return max_dist


print(longest())
# print(longest_recur((rs, cs)))
