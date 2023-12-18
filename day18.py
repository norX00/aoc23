
with open("day18.txt", "r") as of:
    data = of.read().strip()


def gauss_area_formula(edge_points):
    x, y = zip(*edge_points)
    return 0.5 * abs(sum(x[i]*y[i+1] - x[i+1]*y[i] for i in range(len(edge_points)-1)))


def picks_formula(inner, boundary):
    return int(inner + boundary//2 + 1)


def get_polygon_area(instructions):
    current, corners, edge_length = (0, 0), [], 0
    for instruction, steps in instructions:
        edge_length += steps
        corners.append(current)
        match instruction:
            case "R" | "0": current = (current[0] + int(steps), current[1])
            case "L" | "2": current = (current[0] - int(steps), current[1])
            case "D" | "1": current = (current[0], current[1] + int(steps))
            case "U" | "3": current = (current[0], current[1] - int(steps))
    return picks_formula(gauss_area_formula(corners), edge_length)


# Part one
dig_plan = [row.split(" ") for row in data.split("\n")]
print(get_polygon_area((row[0], int(row[1])) for row in dig_plan))

# Part two
print(get_polygon_area((row[2][-2], int(row[2][2:-2], 16)) for row in dig_plan))
