from parse import parse

boxes = [[] for _ in range(9)]
instructions = []
with open("day05.txt") as f:
    instr_flag = False
    for l in f.readlines():
        if l == "\n" or l[0] == " ":
            instr_flag = True
            continue

        if instr_flag:
            p = parse("move {:d} from {:d} to {:d}\n", l)
            instructions += [p.fixed]

        else:
            line_boxes = [l[i] for i in range(1, 35, 4)]
            for i in range(9):
                if (b := line_boxes[i]) != " ":
                    boxes[i] += [b]

print(boxes)
print(instructions)

keep_order = True

for n, start, end in instructions:
    if keep_order:
        b = boxes[start-1][:n]
        boxes[start-1] = boxes[start-1][n:]
        boxes[end-1] = b + boxes[end-1]
    else:
        for _ in range(n):
            b = boxes[start-1].pop(0)
            boxes[end-1] = [b] + boxes[end-1]

print("".join(bs[0] for bs in boxes))