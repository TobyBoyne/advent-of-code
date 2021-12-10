import numpy as np
import re
from collections import defaultdict

with open('day05.txt') as f:
    lines = re.findall('(\d+),(\d+) -> (\d+),(\d+)', f.read())
    points = np.array(lines, dtype=int).reshape((-1, 2, 2))


def vent_count(ignore_diagonals):
    vents = defaultdict(int)

    for p1, p2 in points:
        vector = p2 - p1
        if ignore_diagonals and vector[0] and vector[1]:
            continue
        r = np.abs(vector).max()
        step = vector // r

        for i in range(r + 1):
            vent = tuple(p1 + i * step)
            vents[vent] += 1

    return(sum(ct >= 2 for ct in vents.values()))

print('Part one', vent_count(ignore_diagonals=True))
print('Part two', vent_count(ignore_diagonals=False))