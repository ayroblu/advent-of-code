from utils.file import read_input

contents = read_input(__file__).strip()
# contents = "2333133121414131402"
parts: list[int] = list(map(int, contents))
assert len(parts) % 2 == 1
nums = [int(part) for i, part in enumerate(parts) if i % 2 == 0]
spaces = [int(part) for i, part in enumerate(parts) if i % 2 == 1]
spaces_override: list[list[tuple[int, int]]] = [
    [] for i in range(len(parts)) if i % 2 == 1
]

moved_set = set[int]()
for i, num in reversed(list(enumerate(nums))):
    for s, space in enumerate(spaces):
        if s >= i:
            break
        remaining = space - sum(num for _, num in spaces_override[s])
        if remaining >= num:
            spaces_override[s].append((i, num))
            moved_set.add(i * 2)
            break

total = 0
c = 0
for i, part in enumerate(parts):
    if i in moved_set:
        c += part
        continue
    if i % 2 == 1:
        remaining = part
        for id, num in spaces_override[(i - 1) // 2]:
            total += sum(v for v in range(c, c + num)) * id
            c += num
            remaining -= num
        c += remaining
    else:
        id = i // 2
        total += sum(v for v in range(c, c + part)) * id
        c += part

print(total)
