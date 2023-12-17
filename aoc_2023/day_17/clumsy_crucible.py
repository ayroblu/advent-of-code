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

type CoordWithSum = tuple[
    tuple[int, int], tuple[int, int], int, int, list[tuple[int, int]]
]
seen: dict[tuple[int, int], list[tuple[int, tuple[tuple[int, int], int]]]] = {}

nodes: list[CoordWithSum] = [((0, 0), (0, 1), 0, 0, []), ((0, 0), (1, 0), 0, 0, [])]
while len(nodes):
    (r, c), (rd, cd), cost, same_dir, history = nodes.pop()

    for nrd, ncd in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
        if rd == nrd and cd == ncd and same_dir == 3:
            continue
        if rd == -nrd and cd == -ncd:
            continue
        nr = r + nrd
        nc = c + ncd
        if nr >= len(grid) or nr < 0 or nc >= len(grid[0]) or nc < 0:
            continue
        new_cost = cost + int(grid[nr][nc])
        dir = 1
        if rd == nrd and cd == ncd:
            dir = same_dir + 1
        done = False
        if (nr, nc) in seen:
            for seen_cost, (seen_dir, num_dir) in seen[(nr, nc)]:
                if seen_cost <= new_cost and (nrd, ncd) == seen_dir and num_dir <= dir:
                    done = True
                    break
            else:
                seen[(nr, nc)].append((new_cost, ((nrd, ncd), dir)))
        else:
            seen[(nr, nc)] = [(new_cost, ((nrd, ncd), dir))]
        if done:
            continue
        if nr == len(grid) - 1 and nc == len(grid[0]) - 1:
            # new_grid = [[c for c in line] for line in contents.splitlines()]
            # for r, c in history:
            #     new_grid[r][c] = "x"
            # result = "\n".join(["".join(line) for line in new_grid])

            # print(cost)
            # print(result)
            break
        insort(
            nodes,
            ((nr, nc), (nrd, ncd), new_cost, dir, history + [(nr, nc)]),
            key=(lambda v: -v[2]),
        )
    else:
        continue
    break

print("cost", seen[(len(grid) - 1, len(grid[0]) - 1)][0][0])
