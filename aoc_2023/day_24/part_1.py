import numpy as np
from utils.file import read_input

contents = read_input(__file__)
min_pos = 200000000000000
max_pos = 400000000000000

# contents = """19, 13, 30 @ -2,  1, -2
# 18, 19, 22 @ -1, -1, -2
# 20, 25, 34 @ -2, -2, -4
# 12, 31, 28 @ -1, -2, -1
# 20, 19, 15 @  1, -5, -3"""
# min_pos = 7
# max_pos = 27

type PosVec = tuple[tuple[int, int, int], tuple[int, int, int]]
pos_vecs: list[PosVec] = []
for line in contents.splitlines():
    position, velocity = line.split(" @ ")
    px, py, pz = [int(pos) for pos in position.split(", ")]
    vx, vy, vz = [int(v) for v in velocity.split(", ")]
    pos_vecs.append(((px, py, pz), (vx, vy, vz)))

counter = 0
for i, ((px1, py1, _), (vx1, vy1, _)) in enumerate(pos_vecs):
    for i2, ((px2, py2, _), (vx2, vy2, _)) in enumerate(pos_vecs[i + 1 :]):
        A = np.array([[vx1, -vx2], [vy1, -vy2]])
        b = np.array([px2 - px1, py2 - py1])
        try:
            result = np.linalg.solve(A, b)
            if np.any(result < 0):
                continue
            # vec: px1 + vx1 * result
            if np.any(result < 0):
                continue
            px = px1 + vx1 * result[0]
            py = py1 + vy1 * result[0]
            if min_pos <= px <= max_pos:
                if min_pos <= py <= max_pos:
                    # print(i, i2, px, py)
                    counter += 1
        except:
            pass

print(counter)
