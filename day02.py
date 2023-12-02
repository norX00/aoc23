with open("day2.txt", "r") as of:
    data = of.read().strip()


class Game:
    prio = {"red": 0, "green": 1, "blue": 2}
    limits = [12, 13, 14]

    def __init__(self, hist):
        prefix, sets = hist.split(": ")
        self.id = int(prefix.split(" ")[-1])
        self.sets = self.parse_game(sets)

    def parse_game(self, g):
        units = [
            sorted(
                [unit.split(" ") for unit in s.split(", ")],
                key=lambda x: self.prio.get(x[1]),
            )
            for s in g.split("; ")
        ]
        sets = [[int(num) for num, _ in s] for s in units]
        return sets

    @property
    def is_possible(self):
        possible = all([all([num <= self.limits[idx] for idx, num in enumerate(s)]) for s in self.sets])
        return possible


# Part one
games = [Game(h) for h in data.split("\n")]
print(sum([g.id for g in games if g.is_possible]))
