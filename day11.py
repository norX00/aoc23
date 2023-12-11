from itertools import repeat, combinations

with open("day11.txt", "r") as of:
    data = of.read().strip()


def transpose(field):
    return list(map(lambda x: "".join(x), zip(*field)))


def expand_rows(field):
    return [r for row in field for r in repeat(row, 2 if row.count("#") == 0 else 1)]


def l1_distance(galaxy_pair):
    g1, g2 = galaxy_pair
    return abs(g1[0]-g2[0]) + abs(g1[1]-g2[1])


image = transpose(expand_rows(transpose(expand_rows(data.split("\n")))))
galaxies = [(x, y) for x, row in enumerate(image) for y, cell in enumerate(row) if cell == "#"]

# Part one
print(sum(map(l1_distance, combinations(galaxies, 2))))
