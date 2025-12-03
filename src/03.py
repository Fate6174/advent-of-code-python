from utils.api import get_input
from time import time

input_str = get_input(3)
# input_str = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111
# """

# WRITE YOUR SOLUTION HERE

def compute_batteries(bank : str, num_batteries : int):
    out = 0
    bank_length = len(bank)
    current_idx = 0
    for i in range(num_batteries):
        max_jolt = bank[current_idx]
        for idx, jolt in enumerate(bank[current_idx+1:bank_length-num_batteries+1+i], current_idx+1):
            if jolt > max_jolt:
                current_idx = idx
                max_jolt = jolt
        out += int(max_jolt) * 10 ** (num_batteries-1-i)
        current_idx += 1
    return out

# part 1
tic = time()
out = 0
banks = input_str.splitlines()
for bank in banks:
    out += compute_batteries(bank, 2)
toc = time()
print(f'{toc-tic:.6f} secs: {out}')

# part 2
tic = time()
out = 0
banks = input_str.splitlines()
for bank in banks:
    out += compute_batteries(bank, 12)
toc = time()
print(f'{toc-tic:.6f} secs: {out}')