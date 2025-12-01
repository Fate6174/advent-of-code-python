from utils.api import get_input

input_str = get_input(1)

# WRITE YOUR SOLUTION HERE

# part 1
l1 = list(sorted([int(line.split(' ')[0]) for line in input_str.splitlines()]))
l2 = list(sorted([int(line.split(' ')[3]) for line in input_str.splitlines()]))

res = sum([abs(x-y) for (x,y) in zip(l1,l2)])
print(f'part1: {res}')

# part 2
l1 = [int(line.split(' ')[0]) for line in input_str.splitlines()]
l2 = [int(line.split(' ')[3]) for line in input_str.splitlines()]

res = sum([x if x==y else 0 for x in l1 for y in l2])
print(f'part2: {res}')