from utils.file import read_input
from utils.helpers import mult

contents = read_input(__file__)

mod_types: dict[str, str] = {}
graph: dict[str, list[str]] = {}
rev_graph: dict[str, list[str]] = {}

for line in contents.splitlines():
    id, dest = line.split(" -> ")
    if id == "broadcaster":
        name = id
    else:
        t, name = id[0], id[1:]
        mod_types[name] = t
    dest_list = dest.split(", ")
    graph[name] = dest_list
    for d in dest_list:
        if d in rev_graph:
            rev_graph[d].append(name)
        else:
            rev_graph[d] = [name]

dist_start: dict[str, int] = {}


def get_dist(node: str) -> int:
    if node in dist_start:
        return dist_start[node]
    parents = [p for p in rev_graph[node] if p in mod_types and mod_types[p] == "%"]
    if len(parents) == 0:
        dist_start[node] = 1
        return 1
    elif len(parents) > 1:
        raise Exception("Only one")
    else:
        dist_start[node] = get_dist(parents[0]) + 1
        return dist_start[node]


def get_all_dist(node: str) -> int:
    if mod_types[node] == "%":
        return 2 ** (get_dist(node) - 1)
    else:
        if all(mod_types[n] == "&" for n in rev_graph[node]):
            value = mult(get_all_dist(v) for v in rev_graph[node])
        else:
            value = sum(get_all_dist(v) for v in rev_graph[node])
        print("value", value)
        return value


result = get_all_dist(rev_graph["rx"][0])
print("result", result)
