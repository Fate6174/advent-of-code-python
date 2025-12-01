from utils.api import get_input
import re

input_str = get_input(3)

# WRITE YOUR SOLUTION HERE

# part 1
def f(s : str) -> int:
    l = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', s)

    res = 0
    for x in l:
        y = x.split(',')
        y1 = int(y[0][4:])
        y2 = int(y[1][:-1])
        res += y1*y2
    return res

res = f(input_str)

print(f'part1: {res}')

# part 2
res = 0
while input_str != '':
    idx = input_str.find('don\'t()')
    if idx < 0:
        res += f(input_str)
        input_str = ''
    else:
        res += f(input_str[:idx])
        input_str = input_str[idx+7:]
        idx = input_str.find('do()')
        if idx < 0:
            input_str = ''
        else:
            input_str = input_str[idx+4:]

print(f'part2: {res}')