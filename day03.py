from functools import reduce

with open("day3.txt", "r") as of:
    data = of.read().strip()

numbers, new_number_pos, new_number_str = {}, [], ""
symbols = {}
for idx, line in enumerate(data.split("\n")):
    for jdx, char in enumerate(line):
        if char.isdigit():
            new_number_pos.append((idx, jdx))
            new_number_str += char
        elif new_number_str:
            numbers[tuple(new_number_pos)] = int(new_number_str)
            new_number_pos, new_number_str = [], ""
        if not char.isdigit() and char != ".":
            symbols[(idx, jdx)] = char
    if new_number_str:
        numbers[tuple(new_number_pos)] = int(new_number_str)
        new_number_pos, new_number_str = [], ""


def adjacent(nums_pos, sym_pos):
    return any(
        [
            max(abs(num_pos[0] - sym_pos[0]), abs(num_pos[1] - sym_pos[1])) <= 1
            for num_pos in nums_pos
        ]
    )


# Part one
print(sum([num for coords, num in numbers.items() if any([adjacent(coords, coord) for coord in symbols.keys()])]))


# Part two
def gear_ratio(num_list):
    return reduce(lambda x, y: x * y, num_list) * int(len(num_list) == 2)


print(
    sum(
        [
            gear_ratio([num for coords, num in numbers.items() if any([adjacent(coords, gear_coord)])])
            for gear_coord in [coord for coord, sym in symbols.items() if sym == "*"]
        ]
    )
)
