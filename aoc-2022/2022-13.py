from functools import cmp_to_key

with open("day13.txt") as f:
    lines = [l.strip() for l in f.readlines()]
    pairs = list(zip(lines[::3], lines[1::3]))
    all_signals = lines[::3] + lines[1::3] + ['[[2]]', '[[6]]']

LT = 1
EQ = 0
GT = -1

def comp(a, b):
    if isinstance(a, list) or isinstance(b, list):
        a = a if isinstance(a, list) else [a]
        b = b if isinstance(b, list) else [b]

        for x, y in zip(a, b):
            c = comp(x, y)
            if c == GT:
                return GT
            elif c == LT:
                return LT
        
        return EQ if len(a) == len(b) else LT if len(a) < len(b) else GT
    else:
        # two ints
        return EQ if a == b else LT if a < b else GT

ordered_idxs = []
# pairs = [ ('[[1],[2,3,4]]', '[[1],4]')]
for i, signals in enumerate(pairs):
    sig1, sig2 = map(eval, signals)
    if comp(sig1, sig2) == LT:
        ordered_idxs.append(i + 1)

print(sum(ordered_idxs))

sigs = list(map(eval, all_signals))
sigs_sorted = sorted(sigs, key=cmp_to_key(comp), reverse=True)
div = sigs_sorted.index([[2]]), sigs_sorted.index([[6]])
print((div[0] + 1) * (div[1] + 1))