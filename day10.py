with open("day10.txt", "r") as of:
    data = of.read().strip()

maze = {(x, y): cell for x, row in enumerate(data.split("\n")) for y, cell in enumerate(row) if cell not in "."}


def get_neighbor_coords(x, y, tile=None):
    if tile is None:
        tile = maze[x, y]
    return set({
        "|": [(x-1, y), (x+1, y)],
        "-": [(x, y-1), (x, y+1)],
        "L": [(x-1, y), (x, y+1)],
        "J": [(x-1, y), (x, y-1)],
        "7": [(x+1, y), (x, y-1)],
        "F": [(x+1, y), (x, y+1)],
    }.get(tile, []))


sx, sy = [key for key, val in maze.items() if val == "S"][0]
start_neighbors = [nb for nb in [(sx-1, sy), (sx+1, sy), (sx, sy-1), (sx, sy+1)]
                   if (sx, sy) in get_neighbor_coords(*nb)]
maze[sx, sy] = [t for t in set(maze.values()) if get_neighbor_coords(sx, sy, t) == {*start_neighbors}][0]

# Part one
depth, visited, current = 1, {(sx, sy), *start_neighbors}, start_neighbors[0]
while True:
    next_neighbors = get_neighbor_coords(*current) - visited
    if next_neighbors:
        current = next_neighbors.pop()
    if current in visited:
        print(-(-(depth+1)//2))
        break
    depth += 1
    visited.add(current)
