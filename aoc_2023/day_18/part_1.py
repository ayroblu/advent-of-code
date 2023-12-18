from utils.file import read_input

contents = read_input(__file__)

type Point = tuple[int, int]

r, c = (0, 0)
seen: set[Point] = set()
first = (0, 0)

for line in contents.splitlines():
    dir, num_str, col = line.split()
    num = int(num_str)

    if dir == "U":
        if (r, c) == (0, 0):
            first = (r + 1, c + 1)
        for i in range(num):
            seen.add((r + i + 1, c))
        r += num
    elif dir == "D":
        if (r, c) == (0, 0):
            first = (r - 1, c - 1)
        for i in range(num):
            seen.add((r - i - 1, c))
        r -= num
    elif dir == "L":
        if (r, c) == (0, 0):
            first = (r + 1, c - 1)
        for i in range(num):
            seen.add((r, c - i - 1))
        c -= num
    elif dir == "R":
        if (r, c) == (0, 0):
            first = (r - 1, c + 1)
        for i in range(num):
            seen.add((r, c + i + 1))
        c += num

max_r = max(r for r, _ in seen)
min_r = min(r for r, _ in seen)
max_c = max(c for _, c in seen)
min_c = min(c for _, c in seen)


temp_seen = seen.copy()


def try_fill(points: list[Point], restarted: bool = False) -> None:
    global seen
    restarted = False
    while len(points):
        new_points: list[Point] = []
        for r, c in points:
            for rd, cd in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr, nc = (r + rd, c + cd)
                if not (min_r <= nr <= max_r and min_c <= nc <= max_c):
                    if restarted:
                        raise Exception("Stuck")
                    nr, nc = first
                    seen = temp_seen.copy()
                    return try_fill([(-nr, -nc)], True)
                if (nr, nc) in seen:
                    continue
                seen.add((nr, nc))
                new_points.append((nr, nc))
        points = new_points


try_fill([first])


print(len(seen))
