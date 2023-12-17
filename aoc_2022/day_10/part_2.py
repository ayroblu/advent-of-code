from utils.file import read_input

contents = read_input(__file__)

x = [1]
skip = False
for line in contents.splitlines():
    last = x[-1]
    if line == "noop":
        if not skip:
            x.append(last)
        skip = False
    if line.startswith("addx"):
        _, v = line.split()
        num = int(v)
        if not skip:
            x.append(last)
        x.append(last)
        x.append(last + num)
        skip = True

for i in range(6):
    res: list[str] = []
    for i2 in range(40):
        idx = i * 40 + i2 + 1
        result = "#" if i2 - 1 <= x[idx] <= i2 + 1 else "."
        res.append(result)
    print("".join(res))
