from utils.file import read_file

contents = read_file(__file__, "input")
lines = contents.strip().splitlines()
count = 0

def safe(values: list[int]) -> bool:
    direction = None
    for i, value in enumerate(values):
        if i == 0:
            continue
        prev = values[i-1]
        diff = value - prev
        absdiff = abs(diff)
        if absdiff > 3 or absdiff < 1:
            return False
        if direction == None:
            direction = diff > 0
        elif direction != (diff > 0):
            return False
    return True

for line in lines:
    values = [int(v) for v in line.split(" ")]
    if safe(values):
        count += 1

print(count)
