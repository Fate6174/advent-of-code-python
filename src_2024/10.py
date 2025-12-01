from utils.api import get_input
import numpy as np

input_str = get_input(10)

# WRITE YOUR SOLUTION HERE
map = np.array([[int(c) for c in line] for line in input_str.splitlines()])
m, n = map.shape
# create object array, which will contain paths from the index field in map array to 9's in map array
arr = np.empty(map.shape, dtype='object')
for i, j in zip(*np.where(map != 9)):
    arr[i, j] = []
for i, j in zip(*np.where(map == 9)):
    arr[i, j] = [[(i,j)]]

for k in range(9,0,-1):
    k_idxs = np.where(map == k)
    for i, j in zip(*k_idxs):
        for x, y in [(i-1, j), (i, j+1), (i+1,j), (i,j-1)]:
            if x >= 0 and x < m and y >= 0 and y < n:
                if map[x,y] == k-1:
                    arr[x,y] = arr[x,y] + [[(x,y)] + path for path in arr[i,j]]

trailhead_positions = np.where(map == 0)

# part 1
res = sum([len({path[-1] for path in arr[x,y]}) for x,y in zip(*trailhead_positions)])

print(f'part 1: {res}')

# part 2
res = sum([len(arr[x,y]) for x,y in zip(*trailhead_positions)])

print(f'part 2: {res}')