import re

import numpy as np
from utils.file import read_input

contents = read_input(__file__)

games = contents.split("\n\n")
total = 0
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
    c = [x, y]
    a, b = np.linalg.solve(A, c)
    if abs(a - round(a)) < 2e-13 and abs(b - round(b)) < 2e-13:
        assert a <= 100
        assert b <= 100
        total += round(a * 3 + b)

print(total)
