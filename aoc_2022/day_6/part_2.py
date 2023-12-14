from utils.file import read_input

contents = read_input(__file__)

num = 14
for i in range(num, len(contents)):
    slice = set(contents[i - num : i])
    if len(slice) == num:
        print(i)
        break
