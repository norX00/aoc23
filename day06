from math import ceil, floor, sqrt
from functools import reduce

with open("day6.txt", "r") as of:
    data = of.read().strip()


# Part one
def winning_options(t, d):
    return floor((t+sqrt(t*t-4*d))/2) - ceil((t-sqrt(t*t-4*d))/2) + 1


times, targets = [list(map(int, row.split()[1:])) for row in data.split("\n")]
print(reduce(lambda x, y: x*y, [winning_options(*args) for args in zip(times, targets)]))

# Part two
time, target = [int("".join(x for x in row if x.isdigit())) for row in data.split("\n")]
print(winning_options(time, target))
