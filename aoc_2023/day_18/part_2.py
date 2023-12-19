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
points: list[tuple[int, int]] = []
dirs = {"U": (1, 0), "D": (-1, 0), "L": (0, -1), "R": (0, 1)}

circ = 0
for idx, line in enumerate(contents.splitlines()):
    # dir, num_str, col = line.split()
    # num = int(num_str)
    # rd, cd = dirs[dir]

    _, _, col = line.split()
    hex_dist, dir_key = (col[2:-2], col[-2:-1])
    num = int(hex_dist, 16)
    rd, cd = dirs["RDLU"[int(dir_key)]]

    r += rd * num
    c += cd * num
    points.append((r, c))
    circ += num


# https://stackoverflow.com/questions/451426/how-do-i-calculate-the-area-of-a-2d-polygon
# Basically cross product and divide by 2, the rotation clockwise / counter will cancel out the empty spaces
area = 0
for i in range(1, len(points)):
    (pr, pc), (r, c) = points[i - 1], points[i]
    area += r * pc - c * pr
area = abs(area) // 2
# half of a square + 4 corners, which must rotate to cover 360 aka 1 box
# ###
# ###
# ###
# expand by half of circumfrance + 1 extra. Left and right turns cancel out, eventually always 360 degrees for a closed shape
area = int(area + circ / 2 + 1)


print(area)
