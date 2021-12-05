import numpy as np

with open('day01.txt') as f:
    in_arr = np.array([int(c.strip()) for c in f.readlines()], dtype=int)
    diffs = np.diff(in_arr)
    print((diffs > 0).sum())

    window = np.array([1, 1, 1])
    conv = np.convolve(in_arr, window, mode='valid')
    diffs = np.diff(conv)
    print((diffs > 0).sum())