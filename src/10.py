from utils.api import get_input
from time import time
import numpy as np
import scipy.optimize as sciopt

input_str = get_input(10)
# input_str = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
# """

# WRITE YOUR SOLUTION HERE

# part 1
tic = time()
out = 0
for line in input_str.splitlines():
    a, b = line.split(']')
    target = sum([2 ** idx for idx, c in enumerate(a[1:]) if c == '#'])
    c, d = b.split('{')
    buttons = [sum([2 ** int(num) for num in button[1:-1].split(',')]) for button in c.strip().split(' ')]
    joltage = [int(jolt) for jolt in d[:-1].split(',')]
    num_presses = len(buttons)
    for i in range(2 ** len(buttons)):
        num = 0
        j = i
        for button in buttons:
            if j % 2 > 0:
                num = num ^ button
            j = j // 2
        if num == target:
            num_presses = min(num_presses, i.bit_count())
    out += num_presses
toc = time()
print(f'{toc-tic:.6f} secs: {out}')

# part 2
tic = time()
out = 0
for line in input_str.splitlines():
    a, b = line.split(']')
    c, d = b.split('{')
    buttons = [[int(num) for num in button[1:-1].split(',')] for button in c.strip().split(' ')]
    joltage = [int(jolt) for jolt in d[:-1].split(',')]
    num_presses = len(buttons)
    # set up mixed integer linear programming
    c = np.ones(len(buttons), dtype=int)
    A = np.zeros((len(joltage), len(buttons)), dtype=int)
    for i, button in enumerate(buttons):
        for j in button:
            A[j, i] = 1
    constraints = [sciopt.LinearConstraint(A[idx:idx+1], lb=jolt, ub=jolt) for idx, jolt in enumerate(joltage)]
    milp_result = sciopt.milp(c, integrality=np.ones(len(buttons), dtype=int), constraints=constraints)
    out += int(sum(milp_result.x))
toc = time()
print(f'{toc-tic:.6f} secs: {out}')