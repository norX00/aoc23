from functools import reduce

with open("day4.txt", "r") as of:
    data = of.read().strip()


def parse_nums(num_str: str):
    return set((map(int, filter(lambda x: bool(x), num_str.split(" ")))))


def calc_points(num_set: set):
    return int(2 ** (len(num_set) - 1) * bool(len(num_set)))


# Part one
cards = [c.split(": ")[-1].split(" | ") for c in data.split("\n")]
print(sum([reduce(lambda x, y: calc_points(x & y), map(parse_nums, card)) for card in cards]))
