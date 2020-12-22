cimport numpy as np
cimport cython
import numpy as np

@cython.wraparound(False)
@cython.boundscheck(False)
cpdef run1(np.ndarray[ndim=2, dtype=long] prev_occupied, np.ndarray[ndim=2, dtype=long] can_sit_arr):
	cdef np.ndarray[ndim=2, dtype=long] occupied = np.zeros_like(prev_occupied)
	cdef int can_sit, x, y
	cdef int adj_total

	cdef size_t H = can_sit_arr.shape[0]
	cdef size_t W = can_sit_arr.shape[1]

	cdef long[:, :] can_sit_mv = can_sit_arr
	cdef long[:, :] occupied_mv = occupied


	for y in range(H):
		for x in range(W):
			if not can_sit_mv[y, x]:
				continue

			adj_total = 0
			for j in range(max(y-1,0), min(y+2, H)):
				for i in range(max(x-1,0), min(x+2, W)):
					if not (i==x and j==y):
						adj_total += prev_occupied[j, i]

			if prev_occupied[y, x]:
				occupied_mv[y, x] = 0 if adj_total >= 4 else 1
			else:
				occupied_mv[y, x] = 1 if adj_total == 0 else 0

	return occupied


@cython.wraparound(False)
@cython.boundscheck(False)
cpdef run2(np.ndarray[ndim=2, dtype=long] prev_occupied, np.ndarray[ndim=2, dtype=long] can_sit_arr):
	cdef np.ndarray[ndim=2, dtype=long] occupied = np.zeros_like(prev_occupied)
	cdef int can_sit, x, y
	cdef int can_see_total
	cdef int i, j, dx, dy, a, b

	cdef size_t H = can_sit_arr.shape[0]
	cdef size_t W = can_sit_arr.shape[1]

	cdef long[:, :] can_sit_mv = can_sit_arr
	cdef long[:, :] occupied_mv = occupied

	cdef np.ndarray[ndim=1, dtype=long] ds = np.array([-1, 0, 1])
	cdef long[:] ds_mv = ds

	for y in range(H):
		for x in range(W):
			if not can_sit_mv[y, x]:
				continue

			can_see_total = 0
			for a in range(3):
				for b in range(3):
					dx = ds_mv[a]
					dy = ds_mv[b]
					if dx == dy == 0:
						continue

					i = x + dx
					j = y + dy
					while (0 <= j < H and 0 <= i < W) and not can_sit_mv[j, i]:
						i += dx
						j += dy

					# print(occupied)
					if 0 <= j < H and 0 <= i < W:
						can_see_total += prev_occupied[j, i]

			if prev_occupied[y, x]:
				occupied_mv[y, x] = 0 if can_see_total >= 5 else 1
			else:
				occupied_mv[y, x] = 1 if can_see_total == 0 else 0

	return occupied
