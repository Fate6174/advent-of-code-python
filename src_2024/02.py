from utils.api import get_input

input_str = get_input(2)

# WRITE YOUR SOLUTION HERE

# part 1
def is_safe(l : list[int]) -> bool:
    assert len(l) > 0
    l = [a-b for (a,b) in zip(l[:-1], l[1:])]
    return (all([a < 0 for a in l]) or all([a > 0 for a in l])) and all([abs(a) <= 3 for a in l])

l = [[int(c) for c in line.split(' ')] for line in input_str.splitlines()]

res = sum([1 if is_safe(line) else 0 for line in l])
print(f'part1: {res}')

# part 2
def is_safe2(l : list[int]) -> bool:
    return is_safe(l) or any([is_safe(l[:i] + l[i+1:]) for i in range(len(l))])

l = [[int(c) for c in line.split(' ')] for line in input_str.splitlines()]

res = sum([1 if is_safe2(line) else 0 for line in l])
print(f'part2: {res}')