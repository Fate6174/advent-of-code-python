from utils.api import get_input
from time import time
import numpy as np

input_str = get_input(6)
# input_str = """123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +  
# """

# WRITE YOUR SOLUTION HERE

# part 1
tic = time()
input = [[item for item in line.split(' ') if item != ''] for line in input_str.splitlines()]
nums = np.array([[int(item) for item in line] for line in input[:-1]])
out = 0
for operator, col in zip(input[-1], nums.T):
    if operator == '+':
        out += col.sum()
    else:
        out += col.prod()
toc = time()
print(f'{toc-tic:.6f} secs: {out}')

# part 2
tic = time()
arr = np.array([[c for c in line] for line in input_str.splitlines()])
temp = []
out = 0
for col in arr.T[::-1]:
    num = 0
    for char in col[:-1]:
        if char == ' ':
            continue
        num = 10*num + int(char)
    if num > 0:
        temp += [num]
    if col[-1] != ' ':
        if col[-1] == '+':
            result = 0
            for num in temp:
                result += num
        else:
            result = 1
            for num in temp:
                result *= num
        out += result
        temp = []
toc = time()
print(f'{toc-tic:.6f} secs: {out}')