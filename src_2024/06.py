from utils.api import get_input
import numpy as np

input_str = get_input(6)

# WRITE YOUR SOLUTION HERE

input_array = np.array([list(line) for line in input_str.splitlines()], dtype='object')
m, n = input_array.shape
start_position = np.where((input_array == '^') | (input_array == '>') | (input_array == 'v') | (input_array == '<'))
directions = {
    (-1,0): (-1,0,'^'),
    (0,1): (0,1,'>'),
    (1,0): (1,0,'v'),
    (0,-1): (0,-1,'<')
    }
match input_array[start_position]:
    case '^': start_direction = directions[(-1, 0)]
    case '>': start_direction = directions[(0, 1)]
    case 'v': start_direction = directions[(1, 0)]
    case '<': start_direction = directions[(0, -1)]

# part 1
input_array_copy = input_array.copy()
position = (start_position[0].copy(), start_position[1].copy())
direction = start_direction
input_array_copy[position] = 'X'
res = 1
while True:
    x, y = position
    a, b, c = direction
    
    next = x + a, y + b
    # check if maze is left
    if not (next >= (0,0) and next <= (m-1,n-1)):
        break
    if input_array_copy[next] in ['.', 'X']:
        position = next
        if input_array_copy[next] == '.':
            res += 1
            input_array_copy[next] = 'X'
    elif input_array_copy[next] == '#':
        direction = directions[(b, -a)]

print(f'part 1: {res}')

# part 2
# brute force over all fields where which were traversed in the first run
path_indices = np.where(input_array_copy == 'X')
res = 0
for u, v in zip(*path_indices):
    input_array_copy = input_array.copy()
    position = start_position
    direction = start_direction
    input_array_copy[position] = 'X'
    if input_array_copy[u,v] == '.':
        input_array_copy[u,v] = 'O'
        while True:
            x, y = position
            a, b, c = direction
            next = x + a, y + b
            # check if maze is left
            if next[0] < 0 or next[0] >= m or next[1] < 0 or next[1] >=n:
                break
            # check if loop
            if c in input_array_copy[position][0]:
                res += 1
                break
            # otherwise
            if input_array_copy[next] in ['#', 'O']:
                direction = directions[(b, -a)]
                input_array_copy[position] = input_array_copy[position] + c
            else:
                input_array_copy[position] = input_array_copy[position] + c
                position = next
                if input_array_copy[next] == '.':
                    input_array_copy[next] = 'X'
        input_array_copy[u,v] = '.'

print(f'part 2: {res}')