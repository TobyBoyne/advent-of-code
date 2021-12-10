# cython -a day11.pyx

import numpy as np
import pyximport
pyximport.install(setup_args=dict(include_dirs=[np.get_include()]), language_level=3)
import day11

with open('day11.txt') as f:
	seats = np.array([[c for c in l.rstrip()] for l in f.readlines()])

can_sit_arr = (seats == 'L').astype(np.int)

def run1(prev_occupied, can_sit_arr):
	occupied = np.zeros_like(prev_occupied, dtype=int)
	for (y, x), can_sit in np.ndenumerate(can_sit_arr):
		if can_sit:
			adj = prev_occupied[max(y-1, 0):y+2, max(x-1, 0):x+2]
			if prev_occupied[y, x]:
				occupied[y, x] = 0 if adj.sum() >= 5 else 1
			else:
				occupied[y, x] = 1 if adj.sum() == 0 else 0

	return occupied

# for y, row in enumerate(arr):
# 	print(''.join('#' if c else 'L' if can_sit_arr[y, x] else '.' for x, c in enumerate(row)))

def reach_eq(run_func):
	occupied = np.ones_like(seats, dtype=int)
	next_occupied = np.zeros_like(seats, dtype=int)
	while not np.all(next_occupied == occupied):
		occupied, next_occupied = next_occupied, run_func(next_occupied, can_sit_arr)
	return occupied.sum()

def part_one():
	return reach_eq(day11.run1)

def part_two():
	return reach_eq(day11.run2)


print('Part one', part_one())
print('Part two', part_two())

from time import perf_counter
start_time = perf_counter()
print(reach_eq(run1))
print(f'{(perf_counter()-start_time):.3f} s')


start_time = perf_counter()
print('Part one', part_one())
print(f'{(perf_counter()-start_time):.3f} s')