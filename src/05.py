from utils.api import get_input
from time import time

input_str = get_input(5)
# input_str = """3-5
# 10-14
# 16-20
# 12-18

# 1
# 5
# 8
# 11
# 17
# 32
# """

# WRITE YOUR SOLUTION HERE

# part 1
tic = time()
ranges = [[int(x) for x in line.split('-')] for line in input_str.splitlines() if '-' in line]
ingredients = [int(line) for line in input_str.splitlines() if '-' not in line and line != ""]
out = sum([1 for ingredient in ingredients if any([ingredient >= a and ingredient <= b for [a,b] in ranges])])
toc = time()
print(f'{toc-tic:.6f} secs: {out}')

# part 2
tic = time()
ranges = [[int(x) for x in line.split('-')] for line in input_str.splitlines() if '-' in line]
for idx in range(len(ranges)):
    a, b = ranges[idx]
    to_remove = []
    for idx2 in range(idx):
        if ranges[idx2] is None:
            continue
        c, d = ranges[idx2]
        if d < a or b < c:
            continue
        else:
            a = min(a,c)
            b = max(b,d)
            ranges[idx2] = None
    ranges[idx] = [a,b]
out = sum([range[1] - range[0] + 1 for range in ranges if range is not None])
toc = time()
print(f'{toc-tic:.6f} secs: {out}')