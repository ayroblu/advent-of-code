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


def cut(start_node: str) -> int:
    seen: set[str] = {start_node}
    possible: dict[str, int] = defaultdict(lambda: 0, {k: 1 for k in graph[start_node]})
    min_cut = None
    while len(seen) < len(graph):
        total = sum(possible.values())
        if min_cut == None:
            min_cut = total
        min_cut = min(total, min_cut)
        if total == 3:
            print(len(seen), len(seen) * (len(graph) - len(seen)))
            return min_cut

        next_node, _ = max([(k, v) for k, v in possible.items()], key=lambda x: x[1])

        seen.add(next_node)
        possible.pop(next_node)
        for p in graph[next_node]:
            if p in seen:
                continue
            possible[p] += 1
    if min_cut is None:
        return 0
    return min_cut


# Add all nodes in a stack, pick most "connected" each time


cut(start_node)
