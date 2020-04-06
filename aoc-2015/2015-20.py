import numpy as np
from time import perf_counter

def primes(max_n=1000):
	ns = np.arange(2, max_n)
	primes = np.zeros_like(ns, dtype=bool)
	for i, n in enumerate(ns):
		if np.all(n % ns[:i]):
			primes[i] = True
	return ns[np.where(primes)]


def num_presents(N):
	elves = np.arange(1, N+1)
	presents = elves * (N % elves == 0)
	return 10 * sum(presents)

def smallest_sufficient_multiplier(N):
	"""Returns prime factors (excl. 2) that make up the smallest multiplier
	e.g. x31 would return [3, 7]"""

def part_one(target_presents):
	N = target_presents



scores = np.arange(2, 2*211).reshape(-1, 2) // 2
for i, s in enumerate(scores):
	scores[i, 1] = num_presents(s[1])

print(scores)
print(num_presents(120))
for i in range(1, 1000):
	if (score := num_presents(i)) > 5450:
		print(i)
		break

x = 5 ** 5 * 3 ** 4
x = 2 ** 9
print(num_presents(x * 2 ** 7) / num_presents(x))
"""1/n+1 if n in prime factorisation, else 1/n"""

#
# puzz_input = 33100000
# print(part_one(puzz_input))
#
# x = 33100000 // 10
# print(np.log2(x))