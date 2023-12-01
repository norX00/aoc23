from operator import itemgetter
import re

with open("day1.txt", "r") as of:
    data = of.read().strip()

# Part one
part_one = sum([int("".join(itemgetter(0, -1)([char for char in line if char.isdigit()])))
                for line in data.split("\n")])
print(part_one)

# Part two
digits = r"one|two|three|four|five|six|seven|eight|nine|\d"
digit_map = {d: str(idx + 1) for idx, d in enumerate(digits.split("|")[:-1])}
part_two = sum([int("".join(map(lambda x: digit_map.get(x, x),
                                itemgetter(0, -1)(re.findall(rf"(?=({digits}))", line)),))
                    )
                for line in data.split("\n")])
print(part_two)
