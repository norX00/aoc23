from functools import reduce

with open("day15.txt", "r") as of:
    data = of.read().strip()


def get_hash(current_value, char):
    return (17*(current_value+ord(char))) % 256


# Part one
print(sum(map(lambda z: reduce(lambda x, y: get_hash(x, y), z, 0), data.split(","))))

# Part two - credits reddit/u/4HbQ match statement
boxes = [dict() for _ in range(256)]
for instruction in data.split(","):
    match instruction.strip("-").split("="):
        case [lens, focal]: boxes[reduce(get_hash, lens, 0)][lens] = int(focal)
        case [lens]: boxes[reduce(get_hash, lens, 0)].pop(lens, 0)
print(sum(box_idx * slot * focal for box_idx, box in enumerate(boxes, 1) for slot, focal in enumerate(box.values(), 1)))
