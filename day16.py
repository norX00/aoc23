data = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""

grid = data.split("\n")
grid2 = [list(x) for x in grid[::]]
num_rows, num_cols = len(grid), len(grid[0])


def prettyprint(g):
    for r in g:
        print("".join(r))
    print()


def beam(point_to_directions):
    passed = set()
    while point_to_directions:
        p, direction = point_to_directions.pop()
        while (p, direction) not in passed:
            passed.add((p, direction))
            grid2[p[0]][p[1]] = "#"
            prettyprint(grid2)
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
                    direction = "d"
                    point_to_directions.append((p, "u"))
                case "-":
                    direction = "l"
                    point_to_directions.append((p, "r"))
                case "/":
                    direction = "u" if direction == "r" else "d"
                case "\\":
                    direction = "d" if direction == "r" else "u"
    return passed


beam([((0, 0), "r")])
print(sum(map(lambda x: x.count("#"), grid2)))
