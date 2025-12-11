from utils.api import get_input
from time import time

input_str = get_input(11)
# input_str = """aaa: you hhh
# you: bbb ccc
# bbb: ddd eee
# ccc: ddd eee fff
# ddd: ggg
# eee: out
# fff: out
# ggg: out
# hhh: ccc fff iii
# iii: out
# """
# input_str = """svr: aaa bbb
# aaa: fft
# fft: ccc
# bbb: tty
# tty: ccc
# ccc: ddd eee
# ddd: hub
# hub: fff
# eee: dac
# dac: fff
# fff: ggg hhh
# ggg: out
# hhh: out
# """

# WRITE YOUR SOLUTION HERE

def count_paths(machines: dict[str, list[str]], start: str, end: str, avoid: str, num_pathes: dict[tuple[str, str, str], int]) -> int:
    if (start, end, avoid) in num_pathes.keys():
        return num_pathes[(start, end, avoid)]
    else:
        if start == end:
            num_pathes[(start, end, avoid)] = 1
            return 1
        elif start == avoid or start not in machines.keys():
            num_pathes[(start, end, avoid)] = 0
            return 0
        else:
            out = 0
            for next in machines[start]:
                out += count_paths(machines, next, end, avoid, num_pathes)
            num_pathes[(start, end, avoid)] = out
            return out

# part 1
tic = time()
machines = {}
for line in input_str.splitlines():
    data = line.split(' ')
    machines[data[0][:-1]] = data[1:]
out = count_paths(machines, 'you', 'out', '', {})
toc = time()
print(f'{toc-tic:.6f} secs: {out}')

# part 2
tic = time()
machines = {}
for line in input_str.splitlines():
    data = line.split(' ')
    machines[data[0][:-1]] = data[1:]

num_pathes = {}
svr_to_dac = count_paths(machines, 'svr', 'dac', 'fft', num_pathes)
dac_to_fft = count_paths(machines, 'dac', 'fft', '', num_pathes)
fft_to_out = count_paths(machines, 'fft', 'out', '', num_pathes)
svr_to_fft = count_paths(machines, 'svr', 'fft', 'dac', num_pathes)
fft_to_dac = count_paths(machines, 'fft', 'dac', '', num_pathes)
dac_to_out = count_paths(machines, 'dac', 'out', '', num_pathes)
out = svr_to_dac * dac_to_fft * fft_to_out + svr_to_fft * fft_to_dac * dac_to_out 
toc = time()
print(f'{toc-tic:.6f} secs: {out}')