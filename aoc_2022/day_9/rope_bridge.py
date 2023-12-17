from utils.file import read_input

contents = read_input(__file__)

visited: set[tuple[int, int]] = set()
r, c = (0, 0)
tr, tc = (0, 0)
for line in contents.splitlines():
    dir, num_str = line.split()
    num = int(num_str)
    for _ in range(num):
        if dir == "U":
            r -= 1
            if abs(tr - r) > 1:
                tr = r + 1
                tc = c
        if dir == "D":
            r += 1
            if abs(tr - r) > 1:
                tr = r - 1
                tc = c
        if dir == "L":
            c -= 1
            if abs(tc - c) > 1:
                tr = r
                tc = c + 1
        if dir == "R":
            c += 1
            if abs(tc - c) > 1:
                tr = r
                tc = c - 1
        visited.add((tr, tc))
total = len(visited)
print(total)
