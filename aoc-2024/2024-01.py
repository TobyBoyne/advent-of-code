import numpy as np
from collections import Counter

with open("day01.txt") as f:
    data = f.readlines()

locations = np.array([l.strip().split() for l in data], dtype=int)
locations_l, locations_r = map(np.sort, locations.T)
print(np.sum(np.abs(locations_l - locations_r)))

num_freq = Counter(locations_r)
print(sum(num_freq[x]*x for x in locations_l))