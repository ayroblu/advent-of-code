from utils.file import read_input
from collections import defaultdict

contents = read_input(__file__)

# contents = """jqt: rhn xhk nvd
# rsh: frs pzl lsr
# xhk: hfx
# cmg: qnr nvd lhk bvb
# rhn: xhk bvb hfx
# bvb: xhk hfx
# pzl: lsr hfx nvd
# qnr: nvd
# ntq: jqt hfx bvb xhk
# nvd: lhk
# lsr: lhk
# rzs: qnr cmg lsr rsh
# frs: qnr lhk lsr"""

graph: dict[str, list[str]] = defaultdict(lambda: [])

for line in contents.splitlines():
    name, connected = line.split(": ")
    con_list = connected.split()
    graph[name].extend(con_list)
    for item in con_list:
        graph[item].append(name)

start_node = next(iter(graph))


def cut(start_node: str):
    seen: set[str] = {start_node}
    stack: list[str] = []
    possible: dict[str, int] = defaultdict(lambda: 0, {k: 1 for k in graph[start_node]})
    while len(seen) < len(graph):
        next_node, _ = max([(k, v) for k, v in possible.items()], key=lambda x: x[1])
        seen.add(next_node)
        stack.append(next_node)
        possible.pop(next_node)
        for p in graph[next_node]:
            if p in seen:
                continue
            possible[p] += 1

    other: set[str] = set()
    while len(stack):
        next_node = stack.pop()
        seen.remove(next_node)
        other.add(next_node)
        count = 0
        for node in other:
            for con in graph[node]:
                if con in seen:
                    count += 1
        if count == 3:
            print(len(other), len(seen), len(other) * len(seen))
            return


# Add all nodes in a stack, pick most "connected" each time
# pop back through the stack till num edges = 3


cut(start_node)
