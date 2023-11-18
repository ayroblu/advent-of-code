from utils.file import read_file

contents = read_file(__file__, "input")
lines = contents.split("\n")
maxArr = [0 for _ in range(3)]
current = 0
for line in lines:
    if not line:
        max = maxArr[0]
        if current > max:
            maxArr[0] = current
            maxArr.sort()
        current = 0
        continue

    current += int(line)


print(maxArr)
print(sum(maxArr))
