with open("day2.txt", "r") as of:
    data = of.read().strip()


class Game:
    prio = ["red", "green", "blue"]
    limits = [12, 13, 14]

    def __init__(self, hist):
        prefix, sets = hist.split(": ")
        self.sets_ = sets
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


# Part one
games = [Game(h) for h in data.split("\n")]
print(sum([g.id for g in games if g.is_possible]))
