from typing import Literal, Union

from utils.file import read_input

contents = read_input(__file__)
# contents = """broadcaster -> a, b, c
# %a -> b
# %b -> c
# %c -> inv
# &inv -> a"""
# contents = """broadcaster -> a
# %a -> inv, con
# &inv -> b
# %b -> con
# &con -> output"""

type PulseType = Union[Literal["low"], Literal["high"]]
type State = Union[str, dict[str, PulseType]]
modules: dict[str, tuple[str, list[str], Union[str, dict[str, PulseType]]]] = {}
for line in contents.splitlines():
    name, dest = line.split(" -> ")
    dest_list = dest.split(", ")
    if name == "broadcaster":
        modules[name] = ("", dest_list, "")
    else:
        t, rest = name[0], name[1:]
        state: State = "off" if t == "%" else {}
        modules[rest] = (t, dest_list, state)

for name, (_, dest, state) in modules.items():
    for d in dest:
        if d in modules:
            t, _, state = modules[d]
            if isinstance(state, dict):
                state[name] = "low"


num_low = 0
num_high = 0


def push_button():
    global num_low, num_high
    pulses = [(name, "low", "broadcaster") for name in modules["broadcaster"][1]]
    while len(pulses):
        # print(pulses)
        next_pulses: list[tuple[str, Union[Literal["low"], Literal["high"]], str]] = []
        for name, pt, origin in pulses:
            if pt == "low":
                num_low += 1
            else:
                num_high += 1
            if name in modules:
                t, dest, state = modules[name]
                if t == "%":
                    if pt == "low":
                        if state == "off":
                            next_pulses.extend([(d, "high", name) for d in dest])
                            modules[name] = (t, dest, "on")
                        if state == "on":
                            next_pulses.extend([(d, "low", name) for d in dest])
                            modules[name] = (t, dest, "off")
                if t == "&" and isinstance(state, dict):
                    state[origin] = pt
                    if all(v == "high" for _, v in state.items()):
                        next_pulses.extend([(d, "low", name) for d in dest])
                    else:
                        next_pulses.extend([(d, "high", name) for d in dest])
        pulses = next_pulses


for _ in range(1000):
    num_low += 1
    push_button()
print(num_low, num_high)
print(num_low * num_high)
