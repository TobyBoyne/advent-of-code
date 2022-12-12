def priority(c):
    return ord(c.upper()) - 64 + 26*c.isupper()

with open("aoc-2022/day03.txt") as f:
    t = [[*map(priority, c.strip())] for c in f.readlines()]

splits = [[{*x[:len(x)//2]}, {*x[len(x)//2:]}] for x in t]
print(t)
overlaps = [list(j[0] & j[1])[0] for j in splits]
print(overlaps)
print(sum(overlaps))

group_intersects = [
    list({*t[i]} & {*t[i+1]} & {*t[i+2]})[0]
    for i in range(0, len(t)-1, 3)
]
print(sum(group_intersects))
