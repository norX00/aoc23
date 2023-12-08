from itertools import cycle
from math import lcm

with open("day8.txt", "r") as of:
    data = of.read().strip()

instructions_str, nodes_str = data.split("\n\n")
nodes = {node: nb[1:-1].split(", ") for node, nb in map(lambda x: x.split(" = "), nodes_str.split("\n"))}


def instructions():
    instruction_map = {"L": 0, "R": 1}
    for i in cycle(instructions_str):
        yield instruction_map.get(i)


# Part one
current = "AAA"
for step, instruction in enumerate(instructions(), 1):
    current = nodes.get(current)[instruction]
    if current == "ZZZ":
        print(step)
        break


# Part two
least_common_multiple = 1
for entrance in filter(lambda x: x[-1] == "A", nodes.keys()):
    current = entrance
    for step, instruction in enumerate(instructions(), 1):
        current = nodes.get(current)[instruction]
        if current[-1] == "Z":
            least_common_multiple = lcm(least_common_multiple, step)
            break
print(least_common_multiple)
