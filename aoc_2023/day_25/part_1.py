from utils.file import read_input

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

graph: dict[str, list[str]] = {}

for line in contents.splitlines():
    name, connected = line.split(": ")
    con_list = connected.split()
    if name not in graph:
        graph[name] = []
    graph[name].extend(con_list)
    for item in con_list:
        if item not in graph:
            graph[item] = []
        graph[item].append(name)

start_node = next(iter(graph))


def cut(start_node: str):
    seen: set[str] = {start_node}
    stack: list[str] = []
    while len(seen) < len(graph):
        possible: dict[str, int] = {}
        for node in seen:
            for n in graph[node]:
                if n in seen:
                    continue
                if n not in possible:
                    possible[n] = 0
                possible[n] += 1
        pos = sorted([(k, v) for k, v in possible.items()], key=lambda x: -x[1])
        next_node = pos[0][0]
        seen.add(next_node)
        stack.append(next_node)

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
