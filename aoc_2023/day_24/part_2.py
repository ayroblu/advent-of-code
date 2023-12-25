import numpy as np
import sympy
from utils.file import read_input

contents = read_input(__file__)

# contents = """19, 13, 30 @ -2,  1, -2
# 18, 19, 22 @ -1, -1, -2
# 20, 25, 34 @ -2, -2, -4
# 12, 31, 28 @ -1, -2, -1
# 20, 19, 15 @  1, -5, -3"""

type PosVec = tuple[tuple[int, int, int], tuple[int, int, int]]
pos_vecs: list[PosVec] = []
for line in contents.splitlines():
    position, velocity = line.split(" @ ")
    px, py, pz = [int(pos) for pos in position.split(", ")]
    vx, vy, vz = [int(v) for v in velocity.split(", ")]
    pos_vecs.append(((px, py, pz), (vx, vy, vz)))

# pr + t[i]*v0 == p[i] + t[i]*v[i]
# pr - p[i] = -t[i](vr - v[i])
# # Multiply by cross product. Cross product of itself = 0
# (pr - p[i]) x (vr - v[i]) == 0

# pr x vr - p[i] x vr - pr x v[i] + p[i] x v[i] == 0
# - p[i] x vr - pr x v[i] + p[i] x v[i] == - p[i2] x vr - pr x v[i2] + p[i2] x v[i2]
# - p[i] x vr + vr x p[i2] - pr x v[i] + pr x v[i2] == p[i2] x v[i2] - p[i] x v[i]
# - p[i] x vr + p[i2] x vr + v[i] x pr - v[i2] x pr == p[i2] x v[i2] - p[i] x v[i]


def linarg_solve():
    A = np.zeros((6, 6))
    p0, v0 = pos_vecs[0]
    p1, v1 = pos_vecs[1]
    p2, v2 = pos_vecs[2]
    A[:3, :3] = np.cross(np.identity(3), v0) - np.cross(np.identity(3), v1)
    A[:3, 3:] = -np.cross(np.identity(3), p0) + np.cross(np.identity(3), p1)
    A[3:, :3] = np.cross(np.identity(3), v0) - np.cross(np.identity(3), v2)
    A[3:, 3:] = -np.cross(np.identity(3), p0) + np.cross(np.identity(3), p2)

    b = np.zeros(6)
    b[:3] = np.cross(np.array(p1), np.array(v1)) - np.cross(np.array(p0), np.array(v0))
    b[3:] = np.cross(np.array(p2), np.array(v2)) - np.cross(np.array(p0), np.array(v0))
    result = np.linalg.solve(A, b)

    # print(A)
    print(result)
    print(round(np.sum(result[:3])))


linarg_solve()


def symbolic_solve():
    # No types for sympy
    xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")

    equations = []
    for (px, py, pz), (vx, vy, vz) in pos_vecs:
        equations.append((xr - px) * (vy - vyr) - (yr - py) * (vx - vxr))
        equations.append((yr - py) * (vz - vzr) - (zr - pz) * (vy - vyr))

    result = sympy.solve(equations)[0]
    answer = sum(result[v] for v in [xr, yr, zr])
    print(result)
    print(answer)


symbolic_solve()
