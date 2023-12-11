from utils.file import read_file


contents = read_file(__file__, "input")
lines = contents.splitlines()

expand_r: list[int] = [];
expand_c: list[int] = [];
for r, line in enumerate(lines):
    if not line:
        continue
    if all([l == "." for l in line]):
        expand_r.append(r)
for c, char in enumerate(lines[0]):
    if all([l[c] == "." for l in lines if l[c]]):
        expand_c.append(c)

def insert_str(string: str, str_to_insert: str, index: int) -> str:
    return string[:index] + str_to_insert + string[index:]

expand_r.reverse();
expand_c.reverse();
for r in expand_r:
    lines.insert(r, lines[r])
for c in expand_c:
    for r, line in enumerate(lines):
        lines[r] = insert_str(line, line[c], c)


galaxies: list[tuple[int, int]] = [];
for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if char == "#":
            galaxies.append((r,c))

sum = 0
for i, galaxy in enumerate(galaxies):
    slice = galaxies[(i + 1):]
    for j, g2 in enumerate(slice):
        sum += abs(galaxy[0] - g2[0]) + abs(galaxy[1] - g2[1])

print(sum)
