from utils.file import read_file


contents = read_file(__file__, "input")
lines = contents.splitlines()

expand_r: list[int] = [];
expand_c: list[int] = [];
for r, line in enumerate(lines):
    if all([l == "." for l in line]):
        expand_r.append(r)
for c, char in enumerate(lines[0]):
    if all([l[c] == "." for l in lines if l[c]]):
        expand_c.append(c)

galaxies: list[tuple[int, int]] = [];
for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if char == "#":
            galaxies.append((r,c))

expand = 1000000 - 1
sum = 0
for i, galaxy in enumerate(galaxies):
    slice = galaxies[(i + 1):]
    for j, g2 in enumerate(slice):
        expand_rs = [r for r in expand_r if r < max(galaxy[0], g2[0]) and r > min(galaxy[0], g2[0])]
        expand_cs = [c for c in expand_c if c < max(galaxy[1], g2[1]) and c > min(galaxy[1], g2[1])]
        sum += abs(galaxy[0] - g2[0]) + abs(galaxy[1] - g2[1]) + len(expand_rs) * expand + len(expand_cs) * expand

print(sum)
