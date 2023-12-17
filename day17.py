import heapq

with open("day17.txt", "r") as of:
    data = of.read().strip()


def opposite(d):
    return -d[0], -d[1]


grid = data.split("\n")
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
bottom_right = (len(grid[0]) - 1, len(grid) - 1)
heat_map = {(x, y): int(c) for y, row in enumerate(grid) for x, c in enumerate(row)}


def shortest_path(min_move=1, max_move=3):
    heat, current, direction = 0, (0, 0), (0, 0)
    heap, passed = [(heat, current, direction)], set()
    while heap:
        heat, current, direction = heapq.heappop(heap)
        if current == bottom_right:
            return heat
        if (current, direction) not in passed:
            passed.add((current, direction))
            for direction in [d for d in directions if d not in [direction, opposite(direction)]]:
                p, h = current, heat
                for steps in range(1, max_move + 1):
                    p = p[0] + direction[0], p[1] + direction[1]
                    if p in heat_map:
                        h += heat_map[p]
                        if steps >= min_move:
                            heapq.heappush(heap, (h, p, direction))


# Part one
print(shortest_path())

# Part two
print(shortest_path(4, 10))
