from utils.file import read_input

contents = read_input(__file__).strip()

lines = contents.splitlines()
lr = len(lines)
lc = len(lines[0])

seen = set[tuple[int, int]]()
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def traverse(char: str, coord: tuple[int, int]) -> tuple[int, int]:
    r, c = coord
    area = 1
    perimeter = 0
    for dr, dc in dirs:
        r1, c1 = (r + dr, c + dc)
        if 0 <= r1 < lr and 0 <= c1 < lc:
            if lines[r1][c1] != char:
                perimeter += 1

            if lines[r1][c1] == char:
                if (r1, c1) in seen:
                    continue
                seen.add((r1, c1))

                na, np = traverse(char, (r1, c1))
                area += na
                perimeter += np
        else:
            perimeter += 1
    return area, perimeter


def get_size(char: str, coord: tuple[int, int]) -> int:
    area, perimeter = traverse(char, coord)
    return area * perimeter


total = 0

for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if (r, c) in seen:
            continue
        seen.add((r, c))
        total += get_size(char, (r, c))

print(total)
