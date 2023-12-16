with open("day16.txt", "r") as of:
    data = of.read().strip()

grid = data.split("\n")
nr, nc = len(grid), len(grid[0])  # num rows, num cols


def beam(starting_point_direction):
    energized, passed, point_to_directions = [list(x) for x in grid[::]], set(), [starting_point_direction]
    while point_to_directions:
        p, direction = point_to_directions.pop()
        while (p, direction) not in passed:
            passed.add((p, direction))
            if 0 <= p[0] < nr and 0 <= p[1] < nc:
                energized[p[0]][p[1]] = "#"
            match direction:
                case "r": p = (p[0], p[1] + 1)
                case "l": p = (p[0], p[1] - 1)
                case "u": p = (p[0] - 1, p[1])
                case "d": p = (p[0] + 1, p[1])
            if not (0 <= p[0] < nr and 0 <= p[1] < nc):
                break
            match grid[p[0]][p[1]]:
                case "|":
                    match direction:
                        case "l" | "r":
                            direction = "d"
                            point_to_directions += [(p, "u"), (p, "d")]
                case "-":
                    match direction:
                        case "d" | "u":
                            direction = "l"
                            point_to_directions += [(p, "r"), (p, "l")]
                case "/":
                    match direction:
                        case "r": direction = "u"
                        case "u": direction = "r"
                        case "l": direction = "d"
                        case "d": direction = "l"
                case "\\":
                    match direction:
                        case "r": direction = "d"
                        case "u": direction = "l"
                        case "l": direction = "u"
                        case "d": direction = "r"
    return "".join("".join(x) for x in energized).count("#")


# Part one
print(beam(((0, -1), "r")))

# Part two
pos = [p for lst in [[((-1, i), "d"), ((i, -1), "r"), ((nr, i), "u"), ((i, nc), "l")] for i in range(nc)] for p in lst]
print(max(beam(sp) for sp in pos))
