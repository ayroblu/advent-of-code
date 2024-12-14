import re

from utils.file import read_input

contents = read_input(__file__).strip()
lines = contents.splitlines()

w = 101
h = 103
n = 100

positions = list[tuple[int, int]]()
for line in lines:
    match = re.match(r"p=(\d+),(\d+) v=([+-]?\d+),([+-]?\d+)", line)
    assert match is not None
    x, y, vx, vy = map(int, match.groups())
    x1 = (x + n * vx) % w
    y1 = (y + n * vy) % h
    positions.append((x1, y1))

a, b, c, d = (0, 0, 0, 0)

# x: 0 - 4, 6 - 10 | 11
# y: 0 - 2, 4 - 6 | 7
for x, y in positions:
    if x < w // 2:
        if y < h // 2:
            a += 1
        elif y > h / 2:
            b += 1
    if x > w / 2:
        if y < h // 2:
            c += 1
        elif y > h / 2:
            d += 1

print(a * b * c * d)
