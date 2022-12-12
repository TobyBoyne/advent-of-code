import numpy as np


t = np.loadtxt("aoc-2022/day02.txt", dtype=str)
i = t.view(dtype=int) - np.array([64, 87])
print(i)

w = i[:, 1] + 3 * ((i[:, 1] - i[:, 0] + 1) % 3)
print(w.sum())

scores = 3 * (i[:, 1] - 1)

choices = (i[:, 0] + (i[:, 1] - 3)) % 3 + 1


print(np.sum(scores + choices))