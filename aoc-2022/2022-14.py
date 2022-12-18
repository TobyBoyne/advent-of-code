import numpy as np

with open("day14.txt") as f:
    grid = np.zeros((200, 1000))
    paths_str = [l.strip().split(" -> ") for l in f.readlines()]
    paths = [[tuple(map(int, p.split(","))) for p in path] for path in paths_str]
    for path in paths:
        for p1, p2 in zip(path, path[1:]):
            x, y = min(p1, p2)
            X, Y = max(p1, p2)
            for i in range(x, X+1):
                for j in range(y, Y+1):
                    grid[j, i] = 1


DIRS = [
    1j, -1 + 1j, 1 + 1j
]

walls_per_row = np.sum(grid, axis=1)
EDGE = np.max(np.nonzero(walls_per_row)) + 1

def simulate_sand(grid, floor=False):
    pos = 500 + 0j
    while True:
        for d in DIRS:
            new_pos = pos + d
            x, y = map(int, (new_pos.real, new_pos.imag))
            if y > EDGE:
                if not floor:
                    return new_pos
            elif not grid[y, x]:
                pos = new_pos
                break
        else:
            return pos

filled = False
sand_count = 0
floor = True
while not filled:
    sand_particle = simulate_sand(grid, floor=floor)
    x, y = map(int, (sand_particle.real, sand_particle.imag))
    if (floor and y==0) or (not floor and y > EDGE):
        filled = True
        sand_count += filled
    else:
        sand_count += 1
        grid[y, x] = 1

print(sand_count)