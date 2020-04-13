import numpy as np
import re

DIRECTIONS = {
	'N':	np.array([1, 0]),
	'S':	np.array([-1, 0]),
	'E':	np.array([0, 1]),
	'W':	np.array([0, -1])
}

def read_input():
	with open("day20.txt") as f:
		return f.read()

def get_paths(path_arr):
	if path_arr[0] == '(' and path_arr[-1] == ')':
		path_arr = path_arr[1:-1]
	if '(' not in path_arr:
		return "".join(path_arr).split('|')
	depths = np.zeros(len(path_arr))
	cur_depth = 0
	for i, c in enumerate(path_arr):
		if c == '(':
			cur_depth += 1
		depths[i] = cur_depth == 0
		if c == ')':
			cur_depth -= 1
	print(depths)
	depth_changes = np.where(np.diff(depths))[0]

	print(depth_changes)
	split_arr = np.split(path_arr, depth_changes + 1)
	path = []
	for sub_arr in split_arr:
		path.append(get_paths(sub_arr))

	return path





path_string = "ENWWW(NEEE|SSE(EE|N))EEE"
path_arr = np.array([c for c in path_string])
print(get_paths(path_arr))

def make_grid_from_paths():
	# 3rd dimension of grid represents NSEW doors
	grid = np.zeros((50, 50, 4))