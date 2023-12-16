with open("day16.txt", "r") as of:
    data = of.read().strip()

grid = data.split("\n")
num_rows, num_cols = len(grid), len(grid[0])


def beam(point_to_directions):
    energized = [list(x) for x in grid[::]]
    passed = set()
    while point_to_directions:
        p, direction = point_to_directions.pop()
        while (p, direction) not in passed:
            passed.add((p, direction))
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
            if not (0 <= p[0] < num_rows and 0 <= p[1] < num_cols):
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
    return energized


# Part one
print(sum(map(lambda x: x.count("#"), beam([((0, -1), "r")]))))
