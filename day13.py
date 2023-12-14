with open("day13.txt", "r") as of:
    data = of.read().strip()


def transpose(field):  # day 11
    return list(map(lambda x: "".join(x), zip(*field)))


def hamming_distance(top, bottom):
    return sum(c_top != c_bot for c_top, c_bot in zip(top, bottom))


def find_split(pattern, almost=False):
    for column in range(1, len(pattern)):
        max_size = min(column, len(pattern) - column)
        top_reflected, bottom = pattern[:column][::-1][:max_size], pattern[column:][:max_size]
        if almost and hamming_distance("".join(top_reflected), "".join(bottom)) == 1:
            return column
        if not almost and top_reflected == bottom:
            return column
    return 0


# Part one
patterns = [p.split("\n") for p in data.split("\n\n")]
print(sum(100 * find_split(p) + find_split(transpose(p)) for p in patterns))

# Part two
print(sum(100 * find_split(p, True) + find_split(transpose(p), True) for p in patterns))
