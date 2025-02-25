import re
from collections import defaultdict

from utils.file import read_input

contents = read_input(__file__)

inputs, gates = contents.split("\n\n")

inputs = [input.split(": ") for input in inputs.splitlines()]
regex = r"([\w\d]+) (\w+) ([\w\d]+) -> ([\w\d]+)"
gates = gates.splitlines()

input_map = dict[str, bool]()
for wire, value in inputs:
    input_map[wire] = bool(int(value))


def calc(v1: bool, gtype: str, v2: bool):
    match gtype:
        case "AND":
            return v1 & v2
        case "OR":
            return v1 | v2
        case "XOR":
            return v1 ^ v2
        case _:
            assert False


type Gate = tuple[str, str, str, str]
wires_map = defaultdict[str, list[Gate]](list)
result = 0
for gate in gates:
    match = re.match(regex, gate)
    assert match is not None
    wire1, gtype, wire2, wire3 = match.groups()
    gresult = (wire1, gtype, wire2, wire3)
    if wire1 in input_map and wire2 in input_map:
        input_map[wire3] = calc(input_map[wire1], gtype, input_map[wire2])
        if wire3.startswith("z"):
            pos = int(wire3[1:])
            result |= input_map[wire3] << pos
    else:
        wires_map[wire1].append(gresult)
        wires_map[wire2].append(gresult)

seen = set[Gate]()


def eval_gate(gate: Gate):
    global result
    wire1, gtype, wire2, wire3 = gate
    if wire1 in input_map and wire2 in input_map:
        if gate in seen:
            return
        seen.add(gate)

        input_map[wire3] = calc(input_map[wire1], gtype, input_map[wire2])
        if wire3 in wires_map:
            for gate in wires_map[wire3]:
                eval_gate(gate)
        if wire3.startswith("z"):
            pos = int(wire3[1:])
            result |= input_map[wire3] << pos


for items in wires_map.values():
    for gate in items:
        eval_gate(gate)

print(result)
