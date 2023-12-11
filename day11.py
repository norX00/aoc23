from itertools import repeat, combinations

with open("day11.txt", "r") as of:
    data = of.read().strip()


def transpose(field):
    return list(map(lambda x: "".join(x), zip(*field)))


def expand_rows(field):
    return [r for row in field for r in repeat(row, 2 if row.count("#") == 0 else 1)]


def l1_distance(galaxy_pair):
    g1, g2 = galaxy_pair
    return abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])


orig = data.split("\n")
image = transpose(expand_rows(transpose(expand_rows(orig))))
galaxies = [(x, y) for x, row in enumerate(image) for y, cell in enumerate(row) if cell == "#"]

# Part one
print(sum(map(l1_distance, combinations(galaxies, 2))))

# Part two
horizontal = {x for x, row in enumerate(orig) if row.count("#") == 0}
vertical = {y for y in range(len(orig[0])) if "".join([r[y] for r in orig]).count("#") == 0}
galaxies = {(x, y) for x, row in enumerate(orig) for y, cell in enumerate(row) if cell == "#"}


def crossing_distance(galaxy_pair, crossing_steps=1000000):
    g1, g2 = galaxy_pair
    h_crossings = horizontal & set(range(min(g[0] for g in galaxy_pair), max(g[0] for g in galaxy_pair) + 1))
    v_crossings = vertical & set(range(min(g[1] for g in galaxy_pair), max(g[1] for g in galaxy_pair) + 1))
    return abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) + (crossing_steps - 1) * (len(v_crossings) + len(h_crossings))


print(sum(map(crossing_distance, combinations(galaxies, 2))))
