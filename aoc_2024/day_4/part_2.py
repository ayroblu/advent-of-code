from utils.file import read_file

contents = read_file(__file__, "input")
# contents = """MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX"""
lines = contents.strip().splitlines()

dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
count = 0
for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if char != "A":
            continue
        if r == 0 or r == len(lines) - 1:
            continue
        if c == 0 or c == len(line) - 1:
            continue

        chars = [lines[r + dr][c + dc] for dr, dc in dirs]
        if chars.count('M') != 2 or chars.count('S') != 2:
            continue
        if chars[0] == chars[3]:
            continue
        count += 1

print(count)
