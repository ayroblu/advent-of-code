from collections import defaultdict

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

edges: dict[Point, list[tuple[Point, int]]] = defaultdict(list)

max_dist = 0
seen: set[Point] = {(rs, cs)}


def get_points(point: Point) -> list[Point]:
    r, c = point
    valid_points: list[Point] = []
    for rd, cd in dirs:
        nr, nc = (r + rd, c + cd)
        if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
            continue
        if grid[nr][nc] == "#":
            continue
        valid_points.append((nr, nc))
    return valid_points


def traverse(start_point: Point):
    points = get_points(start_point)
    for point in points:
        if point in seen:
            continue
        seen.add(point)
        traverse_path(start_point, point)


def traverse_path(start_point: Point, point: Point):
    prev_point = start_point
    current_point = point
    dist = 0
    while True:
        dist += 1
        points = [p for p in get_points(current_point) if p != prev_point]
        if len(points) != 1:
            edges[current_point].append((start_point, dist))
            edges[start_point].append((current_point, dist))
            if current_point not in seen:
                seen.add(current_point)
                if len(points) > 0:
                    traverse(current_point)
            return
        seen.add(current_point)
        prev_point = current_point
        current_point = points[0]


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


def longest_recur(point: Point, dist: int) -> int:
    # 12s run time
    if point == (re, ce):
        return dist
    max_dist = 0
    seen.add(point)
    for next_point, next_dist in edges[point]:
        if next_point in seen:
            continue
        l = longest_recur(next_point, dist + next_dist)
        max_dist = max(l, max_dist)
    seen.remove(point)
    return max_dist


edges_arr: list[list[tuple[int, int]]] = []
edge_to_arr: dict[Point, int] = {}


def ensure_default_edge(p: Point):
    if not p in edge_to_arr:
        edge_to_arr[p] = len(edges_arr)
        edges_arr.append([])


for k, v in edges.items():
    ensure_default_edge(k)
    edge_idx = edge_to_arr[k]
    for point, dist in v:
        ensure_default_edge(point)
        point_idx = edge_to_arr[point]
        edges_arr[edge_idx].append((point_idx, dist))

start_idx = edge_to_arr[(rs, cs)]
end_idx = edge_to_arr[(re, ce)]
seen_idx: set[int] = set()


def longest_arr_recur(point: int, dist: int) -> int:
    # 9.8s run time, slightly faster to use idx's over dict but not that much
    if point == end_idx:
        return dist
    max_dist = 0
    seen_idx.add(point)
    for next_point, next_dist in edges_arr[point]:
        if next_point in seen_idx:
            continue
        l = longest_arr_recur(next_point, dist + next_dist)
        max_dist = max(l, max_dist)
    seen_idx.remove(point)
    return max_dist


# print(longest())
# print(longest_recur((rs, cs), 0))
print(longest_arr_recur(start_idx, 0))
