from utils.file import read_input

contents = read_input(__file__)

count = 0
for line in contents.splitlines():
    a, b = line.split(",")
    a1, a2 = map(int, a.split("-"))
    b1, b2 = map(int, b.split("-"))
    if b1 < a1:
        a1, a2, b1, b2 = b1, b2, a1, a2
    if b1 <= a2:
        count += 1

print(count)
