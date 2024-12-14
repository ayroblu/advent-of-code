import re
from time import sleep

from utils.file import read_input

contents = read_input(__file__).strip()
lines = contents.splitlines()

w = 101
h = 103
n0 = 0

positions = dict[tuple[int, int], tuple[int, int]]()
cmds = list[tuple[int, int, int, int]]()
for line in lines:
    match = re.match(r"p=(\d+),(\d+) v=([+-]?\d+),([+-]?\d+)", line)
    assert match is not None
    x, y, vx, vy = map(int, match.groups())
    cmds.append((x, y, vx, vy))

for n in range(n0, 121772):
    frame_pos = set[tuple[int, int]]()
    for x, y, vx, vy in cmds:
        x1 = (x + n * vx) % w
        y1 = (y + n * vy) % h
        frame_pos.add((x1, y1))

    if any(
        sum((p2, p1) in frame_pos for p1 in range(34, 66)) > 12 for p2 in range(0, 50)
    ):
        print(n)
        for i in range(0, h, 2):
            text = [
                "x" if (i, j) in frame_pos or (i + 1, j) in frame_pos else " "
                for j in range(w)
            ]
            print("".join(text))
        print("")
    # print(n)
    # for i in range(h):
    #     text = ["x" if (i, j) in frame_pos else " " for j in range(w)]
    #     print("".join(text))
    # print("")

    # sleep(0.01)
