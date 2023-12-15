from collections import OrderedDict

from utils.file import read_input

contents = read_input(__file__)
# contents = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"


def run_hash(text: str):
    current = 0
    for char in text:
        c = ord(char)
        current += c
        current *= 17
        current %= 256
    return current


boxes: list[OrderedDict[str, str]] = [OrderedDict() for _ in range(256)]
for item in contents.split(","):
    if "=" in item:
        op, value = item.split("=")
        idx = run_hash(op)
        boxes[idx][op] = value
    else:
        op, _ = item.split("-")
        idx = run_hash(op)
        if op in boxes[idx]:
            boxes[idx].pop(op)

sum = 0
for i, box in enumerate(boxes):
    for i2, (_, item) in enumerate(box.items()):
        sum += (i + 1) * (i2 + 1) * int(item)

print(sum)
