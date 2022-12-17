with open("day10.txt") as f:
    instructions = [l.strip().split() for l in f.readlines()]

cycles = 1
pings = list(range(20, 260, 40))
strengths = []
x = 1

img = [[0 for _ in range(40)] for _ in range(6)]

for instr in instructions:
    cmd, *ops = instr

    col, row = (cycles - 1) % 40, (cycles - 1) // 40

    if cmd == "noop":
        if cycles in pings:
            strengths += [cycles * x]
        cycles += 1
        img[row][col] = x - 1 <= col <= x + 1
    else:
        v = int(ops[0])
        for _ in range(2):
            if cycles in pings:
                strengths += [cycles * x]
            cycles += 1
            img[row][col] = x - 1 <= col <= x + 1
            col, row = (cycles - 1) % 40, (cycles - 1) // 40
        x += v

print(sum(strengths))

for row in img:
    print("".join("#" if c else "." for c in row))