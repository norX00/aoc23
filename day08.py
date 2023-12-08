from itertools import cycle
from math import lcm

with open("day8.txt", "r") as of:
    data = of.read().strip()

instructions_str, nodes_str = data.split("\n\n")
nodes = {node: nb[1:-1].split(", ") for node, nb in map(lambda x: x.split(" = "), nodes_str.split("\n"))}


def traverse(entrance, all_z=False):
    def is_exit(e):
        return e == "ZZZ" if all_z else e[-1] == "Z"

    for step, instruction in enumerate(cycle(map("LR".index, instructions_str)), 1):
        entrance = nodes.get(entrance)[instruction]
        if is_exit(entrance):
            return step


# Part one
print(traverse("AAA"))

# Part two
print(lcm(*[traverse(e, False) for e in filter(lambda x: x[-1] == "A", nodes.keys())]))
