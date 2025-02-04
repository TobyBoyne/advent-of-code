import numpy as np
from enum import Enum

class Cell(Enum):
    EMPTY, WALL, GUARD, OOB = range(4)
    VISITED_U, VISITED_R, VISITED_D, VISITED_L = range(4, 8)

def coord(coord: np.ndarray):
    return tuple(coord.flatten())

ROT = np.array([[0, 1], [-1, 0]])
ALL_DIRS = np.array([[0, 1, 0, -1], [-1, 0, 1, 0]])

def direction_to_int(direction: np.ndarray):
    return np.argwhere(np.all(direction == ALL_DIRS, axis=0)).item()
    

guard_pos = -1
with open("day06.txt") as f:
    char_map = dict((c, i) for c, i in zip(".#^", range(3)))
    grid = np.array([[char_map[c] for c in line.strip()] for line in f.readlines() if line.strip()])
    grid = np.pad(grid, 1, constant_values=Cell.OOB.value)
    guard_pos = np.argwhere(grid == Cell.GUARD.value).T
    grid[coord(guard_pos)] = Cell.VISITED_U.value

guard_dir = np.array([[-1, 0]]).T

def run_steps(cur_pos: np.ndarray, cur_dir: np.ndarray, track_loop: bool = False):
    v = 0
    num_obstacles = 0
    while True:
        new_pos = cur_pos + cur_dir
        match grid[coord(new_pos)]:
            case Cell.OOB.value:
                return 0 if track_loop else num_obstacles
            case Cell.WALL.value:
                cur_dir = (ROT @ cur_dir)
            case new_grid_value:
                if not track_loop:
                    # consider putting a wall there
                    track_dir = ROT @ cur_dir
                    if run_steps(cur_pos, track_dir, track_loop=True):
                        num_obstacles += 1
                    grid[coord(new_pos)] = Cell.VISITED_U.value + direction_to_int(cur_dir)
                    v += 1
                    print(v)
                else:
                    # in tracking stage, exit if retracing steps
                    if new_grid_value == Cell.VISITED_U.value + direction_to_int(cur_dir):
                        return 1
                cur_pos = new_pos

num_obstacles = run_steps(guard_pos, guard_dir, track_loop=False)

num_visited = (grid >= Cell.VISITED_U.value).sum()
print(f"{num_visited=}")
print(f"{num_obstacles=}")