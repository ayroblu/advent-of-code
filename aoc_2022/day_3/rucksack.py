from utils.file import read_input

contents = read_input(__file__)

sum = 0
for line in contents.splitlines():
    half = len(line) // 2
    a = line[:half]
    b = line[half:]
    same = set(a).intersection(set(b))
    letter = same.pop()
    s = ord(letter)
    if s >= ord("a"):
        res = s - ord("a") + 1
    else:
        res = s - ord("A") + 27
    sum += res

print(sum)
