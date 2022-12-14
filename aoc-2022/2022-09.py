with open("day09.txt") as f:
    instructions = [l.strip().split() for l in f.readlines()]

def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0


DIRS = {
    "U": 0 + 1j,
    "D": 0 - 1j,
    "R": 1 + 0j,
    "L": -1+ 0j,
}

L = 10
knots = [0j for _ in range(L)]
visited = {0j}

for direction, x in instructions:
    v = DIRS[direction]
    x = int(x)
    for i in range(x):
        knots[0] += v
        for i in range(L-1):
            h, t = knots[i], knots[i+1]
            dx, dy = (h - t).real, (h - t).imag
            if max(abs(dx), abs(dy)) > 1:
                knots[i+1] += sign(dx) + 1j * sign(dy)
        
        visited |= {knots[i+1]}

print(len(visited))