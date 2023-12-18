from utils.file import read_input

contents = read_input(__file__)
# contents = """R 6 (#70c710)
# D 5 (#0dc571)
# L 2 (#5713f0)
# D 2 (#d2c081)
# R 2 (#59c680)
# D 2 (#411b91)
# L 5 (#8ceee2)
# U 2 (#caa173)
# L 1 (#1b58a2)
# U 2 (#caa171)
# R 2 (#7807d2)
# U 3 (#a77fa3)
# L 2 (#015232)
# U 2 (#7a21e3)"""

type Point = tuple[int, int]

r, c = (0, 0)
points: dict[int, list[tuple[int, int]]] = {}

for idx, line in enumerate(contents.splitlines()):
    # dir, num_str, col = line.split()
    # num = int(num_str)

    _, _, col = line.split()
    hex_dist, dir = (col[2:-2], col[-2:-1])
    num = int(hex_dist, 16)

    if dir == "3":
        dir = "U"
    elif dir == "1":
        dir = "D"
    elif dir == "2":
        dir = "L"
    elif dir == "0":
        dir = "R"

    rd, cd = (0, 0)
    if dir == "U":
        rd = 1
    elif dir == "D":
        rd = -1
    elif dir == "L":
        cd = -1
    elif dir == "R":
        cd = 1
    if dir == "U" or dir == "D":
        for i in range(1, num + 1):
            nr, nc = (r + (rd * i), c + (cd * i))
            if nr in points:
                points[nr].append((nc, nc))
            else:
                points[nr] = [(nc, nc)]
    else:
        nc = c + cd * num
        bound = (min(c, nc), max(c, nc))
        if r in points:
            points[r].append(bound)
        else:
            points[r] = [bound]
    r += rd * num
    c += cd * num

print("start")
sum = 0


def around(r: int, part: tuple[int, int]) -> bool:
    c1, c2 = part
    if r - 1 in points and r + 1 in points:
        list_below = [a for p in points[r - 1] for a in list(p)]
        list_above = [a for p in points[r + 1] for a in list(p)]
        if (
            c1 in list_below
            and c2 in list_above
            or c1 in list_above
            and c2 in list_below
        ):
            return True
    return False


def group_sorted_intervals(l: list[tuple[int, int]]) -> list[tuple[int, int]]:
    result: list[tuple[int, int]] = []
    for left, right in l:
        if len(result):
            last_left, last_right = result[-1]
            if left <= last_right:
                result[-1] = (last_left, max(last_right, right))
                continue
        result.append((left, right))
    return result


for r, c in points.items():
    points_list = c
    points_list.sort()
    points_list = group_sorted_intervals(points_list)
    sum += points_list[0][1] - points_list[0][0] + 1
    is_fillable = around(r, points_list[0])
    for i in range(1, len(points_list)):
        sum += points_list[i][1] - points_list[i][0] + 1
        if is_fillable:
            sum += points_list[i][0] - points_list[i - 1][1] - 1
        is_around_current = around(r, points_list[i])
        if is_around_current:
            is_fillable = not is_fillable

print(sum)
