import numpy as np

def primes(max_n=1000):
	n = 2
	while n <= max_n:
		if all(n%i for i in range(2, n)):
			yield n
		n += 1

def num_presents(N):
	elves = np.arange(1, N+1)
	presents = elves * (N % elves == 0)
	return 10 * sum(presents)


def part_one(target_presents):
	N = target_presents / 10 - 1
	initial_guess = 2 ** int(np.log2(target_presents / 10))
	reduce_factor = target_presents/num_presents(initial_guess)
	new_primes = []



x = 5 ** 5 * 3 ** 4
print(num_presents(x) / num_presents(x * 3))
"""1/n+1 if n in prime factorisation, else 1/n"""


puzz_input = 33100000
print(part_one(puzz_input))

x = 33100000 // 10
print(np.log2(x))