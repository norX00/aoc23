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


original = data.split("\n")
expanded = transpose(expand_rows(transpose(expand_rows(original))))
expanded_galaxies = [(x, y) for x, row in enumerate(expanded) for y, cell in enumerate(row) if cell == "#"]

# Part one
print(sum(map(l1_distance, combinations(expanded_galaxies, 2))))

# Part two
horizontal = {x for x, row in enumerate(original) if row.count("#") == 0}
vertical = {y for y, col in enumerate(transpose(original)) if col.count("#") == 0}
galaxies = {(x, y) for x, row in enumerate(original) for y, cell in enumerate(row) if cell == "#"}


def crossing_distance(galaxy_pair, crossing_steps=1000000):
    h_crossings = horizontal & set(range(min(g[0] for g in galaxy_pair), max(g[0] for g in galaxy_pair) + 1))
    v_crossings = vertical & set(range(min(g[1] for g in galaxy_pair), max(g[1] for g in galaxy_pair) + 1))
    return l1_distance(galaxy_pair) + (crossing_steps - 1) * (len(v_crossings) + len(h_crossings))


print(sum(map(crossing_distance, combinations(galaxies, 2))))
