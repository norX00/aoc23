with open("day10.txt", "r") as of:
    data = of.read().strip()

maze = {(x, y): cell for x, row in enumerate(data.split("\n")) for y, cell in enumerate(row) if cell not in "."}
x_max, y_max = max(maze)
start_coords = [(*key, val) for key, val in maze.items() if val == "S"][0]


def get_neighbor_coords(x, y, tile):
    def valid_coords(c):
        return (0 <= c[0] < x_max) and (0 <= c[1] < y_max)
    return list(filter(valid_coords, {
        "|": [(x-1, y), (x+1, y)],
        "-": [(x, y-1), (x, y+1)],
        "L": [(x-1, y), (x, y+1)],
        "J": [(x-1, y), (x, y-1)],
        "7": [(x+1, y), (x, y-1)],
        "F": [(x-1, y), (x, y+1)],
        "S": [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    }.get(tile, [])))


edges, to_visit, visited = [], [start_coords], set()
while to_visit:
    current = to_visit.pop()
    for neighbor_coords in get_neighbor_coords(*current):
        if neighbor_coords not in visited and neighbor_coords in maze:
            to_visit.append((*neighbor_coords, maze[neighbor_coords]))
            edges.append({current[:2], neighbor_coords})
            visited.add(neighbor_coords)

