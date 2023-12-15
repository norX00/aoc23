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


def tilt(p):
    for col_idx in range(num_cols):
        column = rock_sort([row[col_idx] for row in p])
        for row_idx in range(num_rows):
            p[row_idx][col_idx] = column[row_idx]
    return p


# Part one
print(sum(row.count("O") * (num_rows - idx) for idx, row in enumerate(tilt(platform))))
