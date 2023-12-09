with open("day9.txt", "r") as of:
    data = of.read().strip()

histories = [[int(x) for x in ln.split(" ")] for ln in data.split("\n")]


def deltas_dp(hist):
    if sum(map(abs, hist)) == 0:
        return 0
    return deltas_dp([hist[i + 1] - hist[i] for i in range(len(hist) - 1)]) + hist[-1]


# Part one
print(sum(map(deltas_dp, histories)))

# Part two
print(sum(map(deltas_dp, [h[::-1] for h in histories])))
