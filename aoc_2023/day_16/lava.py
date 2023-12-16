from utils.file import read_input

contents = read_input(__file__)
# contents = """.|...\\....
# |.-.\\.....
# .....|-...
# ........|.
# ..........
# .........\\
# ..../.\\\\..
# .-.-/..|..
# .|....-|.\\
# ..//.|...."""
grid = contents.splitlines()

type Coord = tuple[tuple[int, int], tuple[int, int]]
seen: set[Coord] = set()


def has_index(pos: tuple[int, int]) -> bool:
    r, c = pos
    global grid
    return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])


# dir = (r, c)
# right angle at the start
# current = [((0, 0), (0, 1))]
current = [((0, 0), (1, 0))]
energised: set[tuple[int, int]] = set()
while len(current):
    new_current: list[Coord] = []
    for c in current:
        if c in seen:
            continue
        seen.add(c)
        pos, dir = c
        energised.add(pos)
        next: tuple[int, int] = tuple(map(sum, zip(pos, dir)))  # type: ignore
        r, c = next
        if not has_index(next):
            continue
        item = grid[r][c]
        if item == "/":
            rc, rr = dir
            new_current.append((next, (-rr, -rc)))
        elif item == "\\":
            rc, rr = dir
            new_current.append((next, (rr, rc)))
        elif item == "|":
            rr, rc = dir
            if rc != 0:
                new_current.append((next, (-rc, rr)))
                new_current.append((next, (rc, rr)))
            else:
                new_current.append((next, dir))
        elif item == "-":
            rr, rc = dir
            if rr != 0:
                new_current.append((next, (rc, -rr)))
                new_current.append((next, (rc, rr)))
            else:
                new_current.append((next, dir))
        else:
            new_current.append((next, dir))
    new_current = [c for c in new_current if has_index(c[0])]
    current = new_current

print(len(energised))
