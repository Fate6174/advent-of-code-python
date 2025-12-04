from utils.api import get_input
from time import time

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

def find_removables(grid_set : set[complex]) -> list[complex]:
    out = []
    for coordinate in grid_set:
        # count adjacent paper rolls (@)
        adjacent_rolls = 0
        for dz in [-1,1,1j,-1j,1+1j,1-1j,-1+1j,-1-1j]:
            if coordinate + dz in grid_set:
                adjacent_rolls += 1
        if adjacent_rolls < 4:
            out += [coordinate]
    return out

# part 1
tic = time()
# parse input into set containining the coordinates of paper rolls (@)
grid_set = set()
for row_idx, row in enumerate(input_str.splitlines()):
    for col_idx, item in enumerate(row):
        if item == '@':
            grid_set.add(row_idx+col_idx*1j)
out = len(find_removables(grid_set))
toc = time()
print(f'{toc-tic:.6f} secs: {out}')

# part 2
tic = time()
# parse input into set containining the coordinates of paper rolls (@)
grid_set = set()
for row_idx, row in enumerate(input_str.splitlines()):
    for col_idx, item in enumerate(row):
        if item == '@':
            grid_set.add(row_idx+col_idx*1j)
out = 0
while True:
    removables = find_removables(grid_set)
    if removables == []:
        break
    for coordinate in removables:
        grid_set.remove(coordinate)
    out += len(removables)
toc = time()
print(f'{toc-tic:.6f} secs: {out}')