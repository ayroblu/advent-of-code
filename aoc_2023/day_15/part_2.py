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


sum = 0
boxes: list[list[tuple[str, str]]] = [[] for _ in range(256)]
for item in contents.split(","):
    if "=" in item:
        op, value = item.split("=")
        idx = run_hash(op)
        ops = [key for key, _ in boxes[idx]]
        if op not in ops:
            boxes[idx].append((op, value))
        else:
            index = ops.index(op)
            boxes[idx][index] = (op, value)
    else:
        op, _ = item.split("-")
        idx = run_hash(op)
        ops = [key for key, _ in boxes[idx]]
        if op in ops:
            index = ops.index(op)
            del boxes[idx][index]
for i, box in enumerate(boxes):
    for i2, (_, item) in enumerate(box):
        sum += (i + 1) * (i2 + 1) * int(item)

print(sum)
