from utils.file import read_input

contents = read_input(__file__)
# contents = """1,0,1~1,2,1
# 0,0,2~2,0,2
# 0,2,3~2,2,3
# 0,0,4~0,2,4
# 2,0,5~2,2,5
# 0,1,6~2,1,6
# 1,1,8~1,1,9"""

type Coord = tuple[int, int, int]
type Block = tuple[Coord, Coord]
brick_coords: list[Block] = []
for line in contents.splitlines():
    left, right = line.split("~")
    lx, ly, lz = (int(i) for i in left.split(","))
    rx, ry, rz = (int(i) for i in right.split(","))
    brick_coords.append(
        (
            (min(lx, rx), min(ly, ry), min(lz, rz)),
            (max(lx, rx), max(ly, ry), max(lz, rz)),
        )
    )

brick_coords.sort(key=lambda b: b[1][2])


def intersects(a: Block, b: Block) -> bool:
    if b[1][0] >= a[0][0] and a[1][0] >= b[0][0]:
        if b[1][1] >= a[0][1] and a[1][1] >= b[0][1]:
            return True
    return False


intersections: dict[int, set[int]] = {}
supports: dict[int, set[int]] = {}
for i, brick in enumerate(brick_coords):
    matches: set[int] = set()
    max_z = 0
    for i2, brick2 in enumerate(brick_coords[:i]):
        if intersects(brick, brick2):
            matches.add(i2)
            max_z = max(max_z, brick2[1][2])
    matches = {match for match in matches if brick_coords[match][1][2] == max_z}
    intersections[i] = matches
    for match in matches:
        if match not in supports:
            supports[match] = set()
        supports[match].add(i)
    (lx, ly, lz), (rx, ry, rz) = brick
    offset = lz - max_z - 1
    assert lz - offset == max_z + 1
    assert rz - offset > max_z
    brick_coords[i] = ((lx, ly, lz - offset), (rx, ry, rz - offset))

removable: set[int] = set()
for i in range(len(brick_coords)):
    if i in supports:
        if all(len(intersections[s]) != 1 for s in supports[i]):
            removable.add(i)
    else:
        removable.add(i)

# print(
#     [
#         (i, [intersections[s] for s in supports[i]] if i in supports else [])
#         for i in removable
#         if i in supports
#     ]
# )
print(len(removable))
