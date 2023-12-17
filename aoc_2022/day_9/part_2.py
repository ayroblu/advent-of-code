from utils.file import read_input

contents = read_input(__file__)

visited: set[tuple[int, int]] = set()
r, c = (0, 0)
knots: list[tuple[int, int]] = [(0, 0) for _ in range(9)]

for line in contents.splitlines():
    dir, num_str = line.split()
    num = int(num_str)
    for _ in range(num):
        if dir == "U":
            r -= 1
        if dir == "D":
            r += 1
        if dir == "L":
            c -= 1
        if dir == "R":
            c += 1
        (pr, pc) = (r, c)
        for i, (tr, tc) in enumerate(knots):
            if abs(tr - pr) + abs(tc - pc) > 2:
                tr += 1 if pr - tr > 0 else -1
                tc += 1 if pc - tc > 0 else -1
            elif abs(tr - pr) == 2:
                tr += (pr - tr) // 2
            elif abs(tc - pc) == 2:
                tc += (pc - tc) // 2
            knots[i] = (tr, tc)
            (pr, pc) = (tr, tc)
        tr, tc = knots[-1]
        visited.add((tr, tc))
    # print(knots)
total = len(visited)
print(total)
