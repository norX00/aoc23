with open("day12.txt", "r") as of:
    data = of.read().strip()


def parse_rows(row):
    record, occurrences = row.strip().split(" ")
    return record, list(map(int, occurrences.split(",")))


def arrangements_dp(problem):
    record, occurrences = problem
    damaged, lower_bound, upper_bound = sum(occurrences), record.count("#"), record.count("?") + record.count("#")
    if not lower_bound <= damaged <= upper_bound:
        return 0
    if not damaged:
        return 1
    if record[0] == ".":
        return arrangements_dp((record[1:], occurrences))
    if record[0] == "#":
        target = occurrences[0]
        if not record[:target].count(".") and ((len(record) == target) or record[target] != "#"):
            if target == len(record):
                return 1
            return arrangements_dp((record[target + 1:], occurrences[1:]))
        return 0
    return arrangements_dp((record[1:], occurrences)) + arrangements_dp((f"#{record[1:]}", occurrences))


# Part one
print(sum(map(arrangements_dp, map(parse_rows, data.split("\n")))))
