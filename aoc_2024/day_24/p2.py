import re
from collections import defaultdict

from utils.file import read_input

contents = read_input(__file__)

inputs, gates = contents.split("\n\n")

# inputs = [input.split(": ") for input in inputs.splitlines()]
regex = r"([\w\d]+) (\w+) ([\w\d]+) -> ([\w\d]+)"
gates = gates.splitlines()

# input_map = dict[str, bool]()
# for wire, value in inputs:
#     input_map[wire] = bool(int(value))


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
for gate in gates:
    match = re.match(regex, gate)
    assert match is not None
    wire1, gtype, wire2, wire3 = match.groups()
    gresult: Gate = (wire1, gtype, wire2, wire3)
    wires_map[wire1].append(gresult)
    wires_map[wire2].append(gresult)

# Full adder
# 0 digit: XOR 0 0
# 1 digit: XOR (XOR 1 1) (AND 0 0)
# 2 digit: XOR (XOR 2 2) (OR (AND 1 1) (AND (XOR 1 1) (AND 0 0)))

swap = {
    "z13": "vcv",
    "vcv": "z13",
    "z19": "vwp",
    "vwp": "z19",
    "z25": "mps",
    "mps": "z25",
    "vjv": "cqm",
    "cqm": "vjv",
}


def with_swap(wire: str) -> str:
    if wire in swap:
        return swap[wire]
    return wire


def run(input_map: dict[str, bool], seen: set[Gate]):
    result = 0

    def eval_gate(gate: Gate):
        nonlocal result
        wire1, gtype, wire2, wire3 = gate
        if wire1 in input_map and wire2 in input_map:
            if gate in seen:
                return
            seen.add(gate)

            wire3 = with_swap(wire3)
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

    return result


# print(run(input_map))

# x44, y44
# z45
for i in range(45):
    input_map = dict[str, bool]()
    for j in range(45):
        xkey = "x" + str(j).rjust(2, "0")
        input_map[xkey] = False if i != j else True
        ykey = "y" + str(j).rjust(2, "0")
        input_map[ykey] = False if i != j else True

    result = run(input_map, set())
    if result != 1 << (i + 1):
        print(i, result, 1 << (i + 1))

print(",".join(sorted(swap.keys())))
