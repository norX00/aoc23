from itertools import cycle

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
