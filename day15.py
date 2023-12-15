from functools import reduce

with open("day15.txt", "r") as of:
    data = of.read().strip()

# Part one
print(sum(map(lambda z: reduce(lambda x, y: (17 * (x + ord(y))) % 256, z, 0), data.split(","))))
