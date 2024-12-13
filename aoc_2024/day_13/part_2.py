import re

import numpy as np
from utils.file import read_input

contents = read_input(__file__)

games = contents.split("\n\n")
total = 0
offset = 10000000000000
for game in games:
    res = re.match(
        r"""Button A: X[+-](\d+), Y[+-](\d+)
Button B: X[+-](\d+), Y[+-](\d+)
Prize: X=(\d+), Y=(\d+)""",
        game,
    )
    assert res is not None
    ax, ay, bx, by, x, y = map(int, res.groups())
    A = [[ax, bx], [ay, by]]
    c = [x + offset, y + offset]
    a, b = np.linalg.solve(A, c)
    if abs(a - round(a)) < 2e-3 and abs(b - round(b)) < 2e-3:
        total += round(a * 3 + b)

print(total)
