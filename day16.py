with open("day16.txt", "r") as of:
    data = of.read().strip()

grid = data.split("\n")
nr, nc = len(grid), len(grid[0])  # num rows, num cols


def beam(point_to_directions):
    energized, passed = [list(x) for x in grid[::]], set()
    while point_to_directions:
        p, direction = point_to_directions.pop()
        while (p, direction) not in passed:
            passed.add((p, direction))
            if 0 <= p[0] < nr and 0 <= p[1] < nc:
                energized[p[0]][p[1]] = "#"
            match direction:
                case "r":
                    p = (p[0], p[1] + 1)
                case "l":
                    p = (p[0], p[1] - 1)
                case "u":
                    p = (p[0] - 1, p[1])
                case "d":
                    p = (p[0] + 1, p[1])
            if not (0 <= p[0] < nr and 0 <= p[1] < nc):
                break
            match grid[p[0]][p[1]]:
                case "|":
                    match direction:
                        case "l" | "r":
                            direction = "d"
                            point_to_directions.append((p, "u"))
                            point_to_directions.append((p, "d"))
                case "-":
                    match direction:
                        case "d" | "u":
                            direction = "l"
                            point_to_directions.append((p, "r"))
                            point_to_directions.append((p, "l"))
                case "/":
                    match direction:
                        case "r":
                            direction = "u"
                        case "u":
                            direction = "r"
                        case "l":
                            direction = "d"
                        case "d":
                            direction = "l"
                case "\\":
                    match direction:
                        case "r":
                            direction = "d"
                        case "u":
                            direction = "l"
                        case "l":
                            direction = "u"
                        case "d":
                            direction = "r"
    return energized


# Part one
print(sum(map(lambda x: x.count("#"), beam([((0, -1), "r")]))))

# Part two
pos = [p for lst in [[((-1, i), "d"), ((i, -1), "r"), ((nr, i), "u"), ((i, nc), "l")] for i in range(nc)] for p in lst]
print(max(sum(map(lambda x: x.count("#"), beam([sp]))) for sp in pos))
