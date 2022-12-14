cimport numpy as np
cimport cython
import numpy as np

def best_view(np.ndarray[ndim=2, dtype=int] grid):
    
    cdef size_t H = grid.shape[0]
    cdef size_t W = grid.shape[1]

    cdef int[4] DX = [0, 1, 0, -1]
    cdef int[4] DY = [1, 0, -1, 0]

    cdef int cur_size, sight_prod

    cdef np.ndarray[ndim=2, dtype=int] sight_scores = np.zeros_like(grid)

    for y in range(H):
        for x in range(W):
            cur_size = grid[y, x]
            sight_prod = 1
            for dx, dy in zip(DX, DY):
                d = 1
                sightline = 0
                while 0 <= y+dy*d < H and 0 <= x+dx*d < W:
                    sightline += 1
                    if grid[y+dy*d, x+dx*d] >= cur_size:
                        break
                    d += 1
                sight_prod *= sightline
            sight_scores[y, x] = sight_prod
    return sight_scores