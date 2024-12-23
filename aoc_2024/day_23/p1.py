from collections import defaultdict

from utils.file import read_input

contents = read_input(__file__)
lines = contents.splitlines()

graph = defaultdict[str, set[str]](set)

for line in lines:
    left, right = line.split("-")
    graph[left].add(right)
    graph[right].add(left)

count = 0
seen = set[str]()
for key in graph.keys():
    if not key.startswith("t"):
        continue
    seen.add(key)
    seen_loop = set[str]()
    for node in graph[key]:
        if node in seen:
            continue
        if node in seen_loop:
            continue
        seen_loop.add(node)
        for node2 in graph[node]:
            if node2 in seen:
                continue
            if node2 in seen_loop:
                continue
            if key not in graph[node2]:
                continue
            count += 1

print(count)
