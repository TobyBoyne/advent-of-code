WIDTH = 7


class Rock:
    def __init__(self, *shape):
        self.shape = shape
        self.height = max(r.imag for r in shape)
        self.width = max(r.real for r in shape) + 1

    def in_bounds(self, pos: complex):
        return 0 <= pos.real <= WIDTH - self.width

    def intersect(self, pos: complex, settled: set[complex]):
        positions = self.real_positions(pos)
        return pos.imag < 0 or positions.intersection(settled)

    def real_positions(self, pos: complex):
        return {r + pos for r in self.shape}

ROCKS = [
    Rock(0j, 1+0j, 2+0j, 3+0j),         # -
    Rock(1+0j, 0+1j, 1+1j, 2+1j, 1+2j), # +
    Rock(0j, 1+0j, 2+0j, 2+1j, 2+2j),   # L
    Rock(0j, 1j, 2j, 3j),               # |
    Rock(0j, 1+0j, 0+1j, 1+1j),           # o
]

with open("day17.txt") as f:
    jets = [1 if c==">" else -1 for c in f.read()]

# settled_rocks = {x-1j for x in range(WIDTH)}
settled_rocks = set()
highest = -1
step = 0
for i in range(2022):
    rock = ROCKS[i % len(ROCKS)]
    pos = 2 + (highest + 4) * 1j

    while True:
        move = jets[step % len(jets)]
        new_pos = pos + move
        step += 1
        if rock.in_bounds(new_pos) and \
        not rock.intersect(new_pos, settled_rocks):
            pos = new_pos
        
        new_pos = pos - 1j
        if rock.intersect(new_pos, settled_rocks):
            highest = max(highest, int(pos.imag + rock.height))
            settled_rocks |= rock.real_positions(pos)
            break
        else:
            pos = new_pos

def print_tower():
    r = [[False for _ in range(WIDTH)]for _ in range(highest+2)]
    for rock in settled_rocks:
        x, y = map(int, (rock.real, highest - rock.imag))
        print(x, y)
        r[y+1][x] = True

    for row in r: print("".join("#" if c else "." for c in row))
print(highest + 1)