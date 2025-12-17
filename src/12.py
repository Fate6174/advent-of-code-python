from utils.api import get_input
from time import time

input_str = get_input(12)
# input_str = """0:
# ###
# ##.
# ##.

# 1:
# ###
# ##.
# .##

# 2:
# .##
# ###
# ##.

# 3:
# ##.
# ###
# ##.

# 4:
# ###
# #..
# ###

# 5:
# ###
# .#.
# ###

# 4x4: 0 0 0 0 2 0
# 12x5: 1 0 1 0 2 2
# 12x5: 1 0 1 0 3 2
# """

# WRITE YOUR SOLUTION HERE

# FAILS THE TEST INPUT, SUCCEEDS ON THE PUZZLE INPUT
tic = time()
parsed = input_str.split('\n\n')
shapes = [present[3:].splitlines() for present in parsed[:-1]]
areas = [[int(num) for num in line.split(':')[0].split('x')] for line in parsed[-1].splitlines()]
requirements = [[int(num) for num in line.split(':')[1].strip().split(' ')] for line in parsed[-1].splitlines()]
# compute size for each shape
sizes = []
for shape in shapes:
    size = 0
    for line in shape:
        size += line.count('#')
    sizes.append(size)
# check if the areas can accommodate just the size (ignoring the shape) of all required shapes
out = 0
for area, requirement in zip(areas, requirements):
    size_sum = sum([num * sizes[idx] for idx, num in zip(range(1000), requirement)])
    a, b = area
    if size_sum <= a*b:
        out += 1
toc = time()
print(f'{toc-tic:.6f} secs: {out}')