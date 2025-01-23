import re

with open("day03.txt") as f:
    memory = "do()" + f.read() + "don't()"

mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

instructions = re.findall(
    mul_pattern, memory
)
result = sum(int(a) * int(b) for a, b in instructions)
print(result)

dos = re.finditer(r"do\(\)", memory)
donts = re.finditer(r"don't\(\)", memory)

# dos_starts = [do.start(0) for do in dos]
# donts_ends = [dont.end(0) for dont in donts]

valid_ranges = []
cur_range = []
next_do_idx = next(dos).start(0)
next_dont_idx = next(donts).start(0)
while True:
    if next_do_idx < next_dont_idx:
        if not cur_range:
            cur_range.append(next_do_idx)
        
        try:
            next_do_idx = next(dos).start(0)
        except StopIteration:
            valid_ranges.append(cur_range + [next_dont_idx])
            break
    else:
        if cur_range:
            cur_range.append(next_dont_idx)
            valid_ranges.append(cur_range)
            cur_range = []
        next_dont_idx = next(donts).start(0)


enabled_memory = "".join(memory[start:stop] for start, stop in valid_ranges)
instructions = re.findall(
    mul_pattern, enabled_memory
)
result = sum(int(a) * int(b) for a, b in instructions)
print(result)
