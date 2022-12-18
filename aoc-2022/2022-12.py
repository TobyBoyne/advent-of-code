import numpy as np

with open("day12.txt") as f:
    elevs = {"S": "a", "E": "z"}
    grid = []
    start = 0
    target = 0
    for y, line in enumerate(f.readlines()):
        row = []
        for x, c in enumerate(line.strip()):
            elev = ord(elevs.get(c, c)) - ord('a')
            row += [elev]
            if c == "S":
                start = x + 1j*y
            if c == "E":
                target = x + 1j*y
        grid.append(row)
    
    grid = np.array(grid)
    H, W = grid.shape

to_explore = [start]
steps = 0

DS = [1j, -1j, 1+0j, -1+0j]
visited = {start}

while target not in to_explore:
    steps += 1
    prev_explore = to_explore
    to_explore = []
    for p in prev_explore:
        X, Y = map(int, (p.real, p.imag))
        for d in DS:
            new_p = p + d
            x, y = map(int, (new_p.real, new_p.imag))
            if (0 <= y < H) and (0 <= x < W) and (
                grid[y, x] - grid[Y, X] <= 1
            ) and new_p not in visited:
                to_explore.append(new_p)
                visited.add(new_p)

print("part one", steps)

# part two
# start at the target, reach elevation 0

to_explore = [target]
steps = 0

DS = [1j, -1j, 1+0j, -1+0j]
visited = {target}
reached_min_elevation = False

while not reached_min_elevation:
    steps += 1
    prev_explore = to_explore
    to_explore = []
    for p in prev_explore:
        X, Y = map(int, (p.real, p.imag))
        for d in DS:
            new_p = p + d
            x, y = map(int, (new_p.real, new_p.imag))
            if (0 <= y < H) and (0 <= x < W) and (
                - grid[y, x] + grid[Y, X] <= 1
            ) and new_p not in visited:
                to_explore.append(new_p)
                visited.add(new_p)
                if grid[y, x] == 0:
                    reached_min_elevation = True

print("part two", steps)