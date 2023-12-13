from utils.file import read_input

contents = read_input(__file__)

count = 0
for line in contents.splitlines():
    a, b = line.split(",")
    a1, a2 = map(int, a.split("-"))
    b1, b2 = map(int, b.split("-"))
    if a1 <= b1 and a2 >= b2 or b1 <= a1 and b2 >= a2:
        count += 1

print(count)
