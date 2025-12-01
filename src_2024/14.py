from utils.api import get_input
import numpy as np
from PIL import Image

input_str = get_input(14)
m, n = 101, 103

# WRITE YOUR SOLUTION HERE

# part 1
def f(line):
    p, v = line.split(' ')
    p1, p2 = p.split(',')
    p1, p2 = int(p1[2:]), int(p2)
    v1, v2 = v.split(',')
    v1, v2 = int(v1[2:]), int(v2)
    
    p1 = (p1 + 100 * v1) % m
    p2 = (p2 + 100 * v2) % n
    
    match p1, p2:
        case _ if p1 < m // 2 and p2 < n // 2:
            return np.array([1,0,0,0])
        case _ if p1 < m // 2 and p2 > n // 2:
            return np.array([0,1,0,0])
        case _ if p1 > m // 2 and p2 < n // 2:
            return np.array([0,0,1,0])
        case _ if p1 > m // 2 and p2 > n // 2:
            return np.array([0,0,0,1])
        case _:
            return np.array([0,0,0,0])

res = np.prod(sum([f(line) for line in input_str.splitlines()]))

print(res)

# part 2
# strategy: draw images and save to disk to watch at image thumbnails and find the tree
state = np.zeros((m,n), dtype=np.uint8)
robots = np.empty((len(input_str.splitlines()),), dtype='object')
robots_pos_x = np.zeros((len(input_str.splitlines()), 2), dtype=int)
robots_pos_y = np.zeros((len(input_str.splitlines()), 2), dtype=int)
robots_vel_x = np.zeros((len(input_str.splitlines()), 2), dtype=int)
robots_vel_y = np.zeros((len(input_str.splitlines()), 2), dtype=int)
for i, line in enumerate(input_str.splitlines()):
    p, v = line.split(' ')
    p1, p2 = p.split(',')
    p1, p2 = int(p1[2:]), int(p2)
    v1, v2 = v.split(',')
    v1, v2 = int(v1[2:]), int(v2)
    
    robots_pos_x[i] = p1
    robots_pos_y[i] = p2
    robots_vel_x[i] = v1
    robots_vel_y[i] = v2

for i in range(10000):
    print(f'{i}/9999')
    state.fill(0)
    state[robots_pos_x, robots_pos_y] = 255
    
    img = Image.fromarray(state.T)
    img.save(f'src/14_img/{i}.png')
    
    robots_pos_x[:] = (robots_pos_x + robots_vel_x) % m
    robots_pos_y[:] = (robots_pos_y + robots_vel_y) % n