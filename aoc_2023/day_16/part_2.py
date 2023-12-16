from utils.file import read_input

contents = read_input(__file__)
grid = contents.splitlines()

type Coord = tuple[tuple[int, int], tuple[int, int]]


def has_index(pos: tuple[int, int]) -> bool:
    r, c = pos
    global grid
    return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])


# dir = (r, c)
def get_energised(current: list[Coord]) -> int:
    seen: set[Coord] = set()
    energised: set[tuple[int, int]] = set()
    while len(current):
        new_current: list[Coord] = []
        for c in current:
            if c in seen:
                continue
            seen.add(c)
            pos, dir = c
            energised.add(pos)
            r, c = pos
            item = grid[r][c]
            if item == "/":
                rc, rr = dir
                new_current.append((pos, (-rr, -rc)))
            elif item == "\\":
                rc, rr = dir
                new_current.append((pos, (rr, rc)))
            elif item == "|":
                rr, rc = dir
                if rc != 0:
                    new_current.append((pos, (-rc, rr)))
                    new_current.append((pos, (rc, rr)))
                else:
                    new_current.append((pos, dir))
            elif item == "-":
                rr, rc = dir
                if rr != 0:
                    new_current.append((pos, (rc, -rr)))
                    new_current.append((pos, (rc, rr)))
                else:
                    new_current.append((pos, dir))
            else:
                new_current.append((pos, dir))
        new_current: list[Coord] = [
            ((r + rd, c + cd), (rd, cd)) for (r, c), (rd, cd) in new_current
        ]
        new_current = [(pos, dir) for pos, dir in new_current if has_index(pos)]
        current = new_current
    return len(energised)


positions: list[Coord] = [((0, i), (1, 0)) for i in range(len(grid))]
positions += [((len(grid) - 1, i), (-1, 0)) for i in range(len(grid))]
positions += [((i, 0), (0, 1)) for i in range(len(grid[0]))]
positions += [((i, len(grid[0]) - 1), (0, -1)) for i in range(len(grid[0]))]
best = max(get_energised([pos]) for pos in positions)
# best = get_energised([((0, 3), (1, 0))])
print(best)
