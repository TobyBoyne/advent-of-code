from parse import parse
import operator

class Monkey:
    def __init__(self, starting_items, op, test, targets, monkey_lst):
        self.items = starting_items
        self._op = op
        self.test = test
        self.targets = targets #(true, false)
        self.monkey_lst: list['Monkey'] = monkey_lst

        self.inspect_count = 0
        
    def run_op(self, item):
        return eval(self._op.replace("old", str(item)))

    def inspect(self):
        item = self.items.pop(0)
        item = self.run_op(item)
        item //= 3

        if item % self.test == 0:
            target = self.monkey_lst[self.targets[0]]
        else:
            target = self.monkey_lst[self.targets[1]]

        target.catch(item)
        self.inspect_count += 1

    def catch(self, item):
        self.items.append(item)

    def take_turn(self):
        while self.items:
            self.inspect()

with open("day11.txt") as f:
    lines = [l.strip() for l in f.readlines()]
    monkeys: list[Monkey] = []
    for i in range(0, len(lines), 7):
        items = parse("Starting items: {}", lines[i+1]).fixed[0]
        items = list(map(int, items.split(",")))

        op = parse("Operation: new = {}", lines[i+2]).fixed[0]
        # f = operator.add if op_args[1] == "+" else operator.mul
        # nums = op_args[::2]
        # op = lambda x: f(*(x if t=='old' else int(t) for t in nums))

        test = parse("Test: divisible by {:d}", lines[i+3]).fixed[0]

        targets = [parse("If true: throw to monkey {:d}", lines[i+4]).fixed[0],
                parse("If false: throw to monkey {:d}", lines[i+5]).fixed[0]]

        monkeys.append(Monkey(items, op, test, targets, monkeys))

for _ in range(20):
    for monkey in monkeys:
        monkey.take_turn()

for monkey in monkeys:
    print("+", monkey.items)
    print(monkey.inspect_count)