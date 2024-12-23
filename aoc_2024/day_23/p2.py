from collections import defaultdict

from utils.file import read_input

contents = read_input(__file__)
lines = contents.splitlines()

graph = defaultdict[str, set[str]](set)

for line in lines:
    left, right = line.split("-")
    graph[left].add(right)
    graph[right].add(left)


def check(seen_loop: frozenset[str], could_see: set[str]):
    global max_set
    if seen_loop in seen:
        return
    seen.add(seen_loop)
    if len(seen_loop) > len(max_set):
        print("max", len(seen_loop))
        max_set = seen_loop
    if len(could_see) + len(seen_loop) < len(max_set):
        return

    for node in could_see:
        if node in seen_loop:
            continue
        if seen_loop & graph[node] == seen_loop:
            check(
                seen_loop | {node},
                could_see & graph[node],
            )


seen = set[frozenset[str]]()
max_set = set[str]()
for key in graph.keys():
    if not key.startswith("t"):
        continue
    print(key)
    check(frozenset({key}), graph[key])

print(",".join(sorted(list(max_set))))
