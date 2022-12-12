with open("aoc-2022/day04.txt") as f:
    pairs = [l.strip().split(",") for l in f.readlines()]

num_contained = 0
num_overlap = 0

for s1, s2 in pairs:
    a = tuple(map(int, s1.split("-")))
    b = tuple(map(int, s2.split("-")))
    x, y = sorted((a, b), key=lambda x:(x[0], -x[1]))

    num_contained += x[0] <= y[0] <= y[1] <= x[1]
    num_overlap += y[0] <= x[1] 

print(num_contained)
print(num_overlap)

