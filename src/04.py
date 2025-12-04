from utils.api import get_input
from time import time
import numpy as np
import numpy.typing as npt

input_str = get_input(4)
# input_str = """..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.
# """

# WRITE YOUR SOLUTION HERE

def find_removables(grid : npt.NDArray) -> list[tuple[int,int]]:
    m, n = grid.shape
    out = []
    for row_idx in range(m):
        for col_idx in range(n):
            if grid[row_idx,col_idx] == '@':
                # count adjacent paper rolls (@)
                adjacent_rolls = 0
                for i in [-1,0,1]:
                    if row_idx + i in [-1,m]:
                        continue
                    for j in [-1,0,1]:
                        if col_idx + j in [-1,n]:
                            continue
                        if (i,j) != (0,0) and grid[row_idx+i,col_idx+j] == '@':
                            adjacent_rolls += 1
                if adjacent_rolls < 4:
                    out += [(row_idx,col_idx)]
    return out

# part 1
tic = time()
grid = np.array([list(row) for row in input_str.splitlines()])
out = len(find_removables(grid))
toc = time()
print(f'{toc-tic:.6f} secs: {out}')

# part 2
tic = time()
grid = np.array([list(row) for row in input_str.splitlines()])
out = 0
while True:
    removables = find_removables(grid)
    if removables == []:
        break
    for (row_idx, col_idx) in removables:
        grid[row_idx][col_idx] = '.'
    out += len(removables)
toc = time()
print(f'{toc-tic:.6f} secs: {out}')