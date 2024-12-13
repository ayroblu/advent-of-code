from utils.file import read_input

contents = read_input(__file__).strip()

lines = contents.splitlines()
lr = len(lines)
lc = len(lines[0])

seen = set[tuple[int, int]]()
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
diag_dirs = [(1, 1), (-1, -1), (1, -1), (-1, 1)]


def traverse(char: str, coord: tuple[int, int]) -> tuple[int, int]:
    r, c = coord
    area = 1
    edges = list[int]()
    corners = 0
    for d, (dr, dc) in enumerate(dirs):
        r1, c1 = (r + dr, c + dc)
        if 0 <= r1 < lr and 0 <= c1 < lc:
            if lines[r1][c1] != char:
                edges.append(d)

            if lines[r1][c1] == char:
                if (r1, c1) in seen:
                    continue
                seen.add((r1, c1))

                na, nc = traverse(char, (r1, c1))
                area += na
                corners += nc
        else:
            edges.append(d)
    if len(edges) <= 2:
        for dr, dc in diag_dirs:
            r1, c1 = (r + dr, c)
            r2, c2 = (r, c + dc)
            r3, c3 = (r + dr, c + dc)
            if not (0 <= r1 < lr and 0 <= c1 < lc):
                continue
            if not (0 <= r2 < lr and 0 <= c2 < lc):
                continue
            if not (0 <= r3 < lr and 0 <= c3 < lc):
                continue
            if lines[r1][c1] == char and lines[r2][c2] == char:
                if char != lines[r3][c3]:
                    corners += 1
    if len(edges) == 2:
        a, b = edges
        if (a == 0 and b == 1) or (a == 2 and b == 3):
            pass
        else:
            corners += 1
    elif len(edges) == 3:
        corners += 2
    elif len(edges) == 4:
        corners += 4
    return area, corners


def get_size(char: str, coord: tuple[int, int]) -> int:
    area, corners = traverse(char, coord)
    return area * corners


total = 0

for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if (r, c) in seen:
            continue
        seen.add((r, c))
        total += get_size(char, (r, c))

print(total)
