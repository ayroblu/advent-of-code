from utils.file import read_input

contents = read_input(__file__).strip()
# contents = "2333133121414131402"
parts: list[int] = list(map(int, contents))
assert len(parts) % 2 == 1
last_id = (len(contents) - 1) // 2
last_idx = len(contents) - 1

total = 0
c = 0
ei = last_idx
for i, part in enumerate(parts):
    if i > ei:
        break
    if i % 2 == 1:
        remaining = part
        while remaining > 0:
            id = ei // 2
            to_sum = min(parts[ei], remaining)
            total += sum(v for v in range(c, c + to_sum)) * id
            c += to_sum
            remaining -= to_sum
            parts[ei] -= to_sum
            if parts[ei] == 0:
                ei -= 2
                if i > ei:
                    break
    else:
        id = i // 2
        total += sum(v for v in range(c, c + part)) * id
        c += part

print(total)
