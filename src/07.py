from utils.api import get_input
from time import time
import numpy as np

input_str = get_input(7)
# input_str = """.......S.......
# ...............
# .......^.......
# ...............
# ......^.^......
# ...............
# .....^.^.^.....
# ...............
# ....^.^...^....
# ...............
# ...^.^...^.^...
# ...............
# ..^...^.....^..
# ...............
# .^.^.^.^.^...^.
# ...............
# """

# WRITE YOUR SOLUTION HERE

def fill_manifold(input_str : str) -> tuple[int, np.typing.NDArray]:
    manifold = np.array([[c for c in line] for line in input_str.splitlines()])
    m, n = manifold.shape
    beam_positions = [tuple([int(n) for n in start]) for start in np.argwhere(manifold == 'S')]
    out = 0
    while beam_positions != []:
        a, b = beam_positions.pop()
        if a == m-1:
            continue
        match manifold[a+1,b]:
            case '.':
                manifold[a+1,b] = '|'
                beam_positions.append((a+1,b))
            case '^':
                out += 1
                if b > 0 and manifold[a+1,b-1] == '.':
                    beam_positions.append((a,b-1))
                if b < n-1 and manifold[a+1,b+1] == '.':
                    beam_positions.append((a,b+1))
    return out, manifold

# part 1
tic = time()
out, _ = fill_manifold(input_str)
toc = time()
print(f'{toc-tic:.6f} secs: {out}')

# part 2
tic = time()
_, manifold = fill_manifold(input_str)
m, n = manifold.shape
cache = {}
for j in range(n):
    if manifold[m-1,j] == '|':
        cache[(m-1, j)] = 1
for i in range(m-2,0,-1):
    for j in range(n):
        if manifold[i, j] == '|':
            if manifold[i+1,j] == '|':
                cache[(i,j)] = cache[(i+1,j)]
            if manifold[i+1,j] == '^':
                cache[(i,j)] = 0
                if j > 0:
                    cache[(i,j)] += cache[(i+1,j-1)]
                if j < n-1:
                    cache[(i,j)] += cache[(i+1,j+1)]
beam_starts = [[int(n) for n in start] for start in np.argwhere(manifold == 'S')]
out = 0
for [a,b] in beam_starts:
    out += cache[(a+1,b)]
toc = time()
print(f'{toc-tic:.6f} secs: {out}')