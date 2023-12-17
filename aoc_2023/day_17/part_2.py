from bisect import insort

from utils.file import read_input

contents = read_input(__file__)
# contents = """2413432311323
# 3215453535623
# 3255245654254
# 3446585845452
# 4546657867536
# 1438598798454
# 4457876987766
# 3637877979653
# 4654967986887
# 4564679986453
# 1224686865563
# 2546548887735
# 4322674655533"""

grid = contents.splitlines()

type CoordWithSum = tuple[tuple[int, int], tuple[int, int], int, int]
seen: dict[tuple[tuple[int, int], tuple[int, int]], list[tuple[int, int]]] = {}

nodes: list[CoordWithSum] = [((0, 0), (0, 1), 0, 0), ((0, 0), (1, 0), 0, 0)]
while len(nodes):
    (r, c), (rd, cd), cost, same_dir = nodes.pop()
    if (r, c) == (len(grid) - 1, len(grid[0]) - 1):
        print("cost", cost)
        break

    for nrd, ncd in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
        if (rd, cd) == (nrd, ncd) and same_dir == 10:
            continue
        if (rd, cd) == (-nrd, -ncd):
            continue
        if (rd, cd) != (nrd, ncd) and same_dir < 4:
            continue

        nr = r + nrd
        nc = c + ncd
        if (rd, cd) != (nrd, ncd):
            # if turning, need to check 4 ahead
            nr = r + nrd * 4
            nc = c + ncd * 4
        if nr >= len(grid) or nr < 0 or nc >= len(grid[0]) or nc < 0:
            continue

        new_cost = cost + int(grid[nr][nc])
        if (rd, cd) != (nrd, ncd):
            # also adjust the cost
            new_cost = cost
            for i in range(4):
                new_cost += int(grid[r + nrd * (i + 1)][c + ncd * (i + 1)])

        dir = 4
        if (rd, cd) == (nrd, ncd):
            dir = same_dir + 1

        done = False
        seen_key = ((nr, nc), (nrd, ncd))
        if seen_key in seen:
            for seen_cost, num_dir in seen[seen_key]:
                if seen_cost <= new_cost and num_dir <= dir:
                    done = True
                    break
            else:
                seen[seen_key].append((new_cost, dir))
        else:
            seen[seen_key] = [(new_cost, dir)]
        if done:
            continue

        insort(
            nodes,
            ((nr, nc), (nrd, ncd), new_cost, dir),
            key=(lambda v: -v[2]),
        )
