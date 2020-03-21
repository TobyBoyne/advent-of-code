from itertools import permutations as pmt

puzz_input = [[int(n) for n in line.split("\t")] for line in open("day2.txt", 'r').read().split("\n")]

checksum = lambda S:sum(max(line) - min(line) for line in S)
print(checksum(puzz_input))

even_div = lambda S:sum([a//b for a, b in pmt(line, 2) if not a%b][0] for line in S)
print(even_div(puzz_input))