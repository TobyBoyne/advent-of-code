from operator import add, mul

def concat(a, b):
    return int(str(a) + str(b))

equations = []
with open("day07.txt") as f:
    for line in f.readlines():
        target, numbers = line.split(":", maxsplit=1)
        equations.append(
            (int(target), list(map(int, numbers.split())))
        )

def verify_equation(target, numbers, ops):
    if len(numbers) == 1:
        return target == numbers[0]
    
    new_lsts = [
        [op(numbers[0], numbers[1])] + numbers[2:]
        for op in ops
    ]
    return any(verify_equation(target, lst, ops) for lst in new_lsts)


TWO_OPS = [add, mul]
THREE_OPS = [add, mul, concat]
true_two_ops = 0
true_three_ops = 0
for equation in equations:
    print(equation)
    target, numbers = equation
    true_two_ops += target * verify_equation(target, numbers, ops=TWO_OPS)
    true_three_ops += target * verify_equation(target, numbers, ops=THREE_OPS)

print(f"{true_two_ops=}")
print(f"{true_three_ops=}")