import numpy as np

adj = np.zeros((100, 100))
updates = []
with open("day05.txt") as f:
    while True:
        line = f.readline()
        if line == "\n": break
        a, b = map(int, line.split("|"))
        adj[a, b] = 1

    while True:
        line = f.readline()
        if line == "\n" or not line: break
        updates.append(list(map(int, line.split(","))))

# if adj[a, b] == 1, then a must come before b

# validate correct order
def validate(update):
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            if adj[update[j], update[i]] == 1:
                return False
    return True

def reordered_middle_val(update):
    arr = adj[np.ix_(update, update)]
    # arr is symmetric, so doesn't matter which axis you sum over
    mid_idx = np.argwhere(arr.sum(axis=1) == len(update) // 2).item()
    return update[mid_idx]

valid_middle_page_sum = 0
invalid_middle_page_sum = 0
for update in updates:
    if validate(update):
        valid_middle_page_sum += update[len(update) // 2]
    else:
        middle = reordered_middle_val(update)
        invalid_middle_page_sum += middle

print(f"{valid_middle_page_sum=}")
print(f"{invalid_middle_page_sum=}")