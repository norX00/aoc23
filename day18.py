
with open("day18.txt", "r") as of:
    data = of.read().strip()


def gauss_area_formula(edge_points):
    x, y = zip(*edge_points)
    return 0.5 * abs(sum(x[i]*y[i+1] - x[i+1]*y[i] for i in range(len(edge_points)-1)))


def picks_formula(inner, boundary):
    return int(inner + boundary//2 + 1)


current, visited, edge_length = (0, 0), [], 0
for instruction, steps, _ in [row.split(" ") for row in data.split("\n")]:
    edge_length += int(steps)
    for _ in range(int(steps)):
        visited.append(current)
        match instruction:
            case "R": current = (current[0]+1, current[1])
            case "L": current = (current[0]-1, current[1])
            case "D": current = (current[0], current[1]+1)
            case "U": current = (current[0], current[1]-1)


# Part one
print(picks_formula(gauss_area_formula(visited), edge_length))

# Part two
current, corners, edge_length = (0, 0), [], 0
for _, _, code in [row.split(" ") for row in data.split("\n")]:
    instruction, steps = [int(code[-2]), int(code[2:-2], 16)]
    edge_length += int(steps)
    corners.append(current)
    match instruction:
        case 0: current = (current[0]+int(steps), current[1])
        case 2: current = (current[0]-int(steps), current[1])
        case 1: current = (current[0], current[1]+int(steps))
        case 3: current = (current[0], current[1]-int(steps))
print(picks_formula(gauss_area_formula(corners), edge_length))
