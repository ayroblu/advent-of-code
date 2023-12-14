from utils.file import read_input

contents = read_input(__file__)

for i in range(4, len(contents)):
    slice = set(contents[i - 4 : i])
    if len(slice) == 4:
        print(i)
        break
