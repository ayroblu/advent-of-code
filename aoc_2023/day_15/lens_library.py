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
for item in contents.split(","):
    result = run_hash(item)
    sum += result
print(sum)
