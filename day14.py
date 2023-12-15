with open("day14.txt", "r") as of:
    data = of.read().strip()

platform = [list(row) for row in data.split("\n")]
num_rows, num_cols = len(platform), len(platform[0])


def rock_sort(col):
    col_before = []
    while col_before != col:
        col_before = col[::]
        for i in range(num_rows - 1):
            if col[i + 1] == "O" and col[i] not in "O#":
                col[i], col[i + 1] = col[i + 1], col[i]
    return col


def tilt(p, rotate_90=False):
    for col_idx in range(num_cols):
        column = rock_sort([row[col_idx] for row in p])
        for row_idx in range(num_rows):
            p[row_idx][col_idx] = column[row_idx]
    if rotate_90:
        p = [list(x) for x in zip(*p[::-1])]  # turn 90 deg by transposing horizontal mirror
    return p


def calculate_score(p):
    return sum(row.count("O") * (num_rows - row_idx) for row_idx, row in enumerate(p))


# Part one
print(calculate_score(tilt(platform)))


# Part two
cycle_idx, cycle_score, idx = dict(), dict(), 0
while True:
    # Run through until cycle repeats itself, then calculate pattern and score at 1 billion
    pattern = str("".join("".join(row) for row in platform))
    if pattern in cycle_idx:
        break
    cycle_idx[pattern], cycle_score[idx] = idx, calculate_score(platform)
    for _ in range(4):
        platform = tilt(platform, rotate_90=True)
    idx += 1
final_idx = cycle_idx[pattern] + (1000000000 - cycle_idx[pattern]) % (idx - cycle_idx[pattern])
print(cycle_score[final_idx])
