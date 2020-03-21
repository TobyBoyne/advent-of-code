puzz_input = open("day1.txt", 'r').read().strip("\n")

part_one = lambda S:sum(int(x) for i, x in enumerate(S) if x == S[i-1])
print(part_one(puzz_input))

part_two = lambda S:sum(int(x) for i, x in enumerate(S) if x == S[i - len(S)//2])
print(part_two(puzz_input))