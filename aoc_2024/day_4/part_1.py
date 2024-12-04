from utils.file import read_file

contents = read_file(__file__, "input")
lines = contents.strip().splitlines()

dirs = [0, 1, -1]
count = 0
for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if char != "X":
            continue
        for dirR in dirs:
            for dirC in dirs:
                r1 = r
                c1 = c
                for letter in "MAS":
                    r1 += dirR
                    c1 += dirC
                    if r1 < 0 or r1 >= len(lines):
                        break
                    if c1 < 0 or c1 >= len(line):
                        break
                    char1 = lines[r1][c1]
                    if char1 != letter:
                        break
                else:
                    count += 1

print(count)
