from functools import reduce

with open("day2.txt", "r") as of:
    data = of.read().strip()


class Game:
    prio = ["red", "green", "blue"]
    limits = [12, 13, 14]

    def __init__(self, hist):
        prefix, sets = hist.split(": ")
        self.id = int(prefix.split(" ")[-1])
        self.sets = self.parse_game(sets)

    def parse_game(self, g):
        units = [
            {
                color: int(num)
                for num, color in [unit.split(" ") for unit in s.split(", ")]
            }
            for s in g.split("; ")
        ]
        sets = [[s.get(col, 0) for col in self.prio] for s in units]
        return sets

    @property
    def is_possible(self):
        possible = all(
            [
                all([num <= self.limits[idx] for idx, num in enumerate(s)])
                for s in self.sets
            ]
        )
        return possible

    @property
    def minimum_requirements(self):
        return [max([el[i] for el in self.sets]) for i in range(3)]

    @property
    def power(self):
        return reduce(lambda x, y: x * y, self.minimum_requirements)


# Part one
games = [Game(h) for h in data.split("\n")]
print(sum([g.id for g in games if g.is_possible]))

# Part two
print(sum([g.power for g in games]))
