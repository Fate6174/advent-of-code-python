from utils.api import get_input
from time import time
import numpy as np

input_str = get_input(9)
# input_str = """7,1
# 11,1
# 11,7
# 9,7
# 9,5
# 2,5
# 2,3
# 7,3
# """

# WRITE YOUR SOLUTION HERE

# part 1
tic = time()
coords = [tuple([int(num) for num in line.split(',')]) for line in input_str.splitlines()]
out = 0
for idx, (a,b) in enumerate(coords):
    for c,d in coords[idx+1:]:
        area = (abs(a-c) + 1) * (abs(b-d) + 1)
        out = max(out, area)
toc = time()
print(f'{toc-tic:.6f} secs: {out}')

# part 2
tic = time()
coords = [tuple([int(num) for num in line.split(',')]) for line in input_str.splitlines()]

def is_inside(polygon : list[tuple[int,...]], point : tuple[int, int]) -> bool:
    out = False
    x0, y0 = point
    for i in range(len(polygon)):
        j = (i + 1) % len(polygon)
        x1, y1 = polygon[i]
        x2, y2 = polygon[j]
        if x1 != x2:
            if x0 >= min(x1,x2) and x0 <= max(x2,x2) and y0 == y1:
                return True
        if y0 >= min(y1, y2) and y0 <= max(y1, y2):
            if x0 == x1:
                return True
            if x0 <= x1:
                out = not out
    return out

out = 0
num_rectangles = len(coords) * (len(coords) + 1) // 2
rect = 1
inside_dict = {}
for (a,b), (c,d) in zip(coords, coords[1:] + coords[:1]):
    if a == c:
        for (x,y) in [(a, col) for col in range(min(b,d),max(b,d)+1)]:
            inside_dict[(x,y)] = True
    elif b == d:
        for (x,y) in [(row, b) for row in range(min(a,c),max(a,c)+1)]:
            inside_dict[(x,y)] = True
    else:
        raise ValueError()
for idx, (a,b) in enumerate(coords):
    for (c,d) in coords[idx+1:]:
        print(f'{rect}/{num_rectangles}')
        rect += 1
        # rectangle A = [a,b] -> [c,b] -> [c,d] -> [a,d]
        area = (abs(a-c) + 1) * (abs(b-d) + 1)
        if area <= out:
            continue
        # test every point on the boundary of the rectangle A
        # if it lies withing the polygon P
        if a == c:
            boundary = [(a, col) for col in range(min(b,d),max(b,d)+1)]
        elif b == d:
            boundary = [(row, b) for row in range(min(a,c),max(a,c)+1)]
        else:
            boundary = ([(row, b) for row in range(min(a,c),max(a,c)+1)] +
                [(row, d) for row in range(min(a,c),max(a,c)+1)] +
                [(a, col) for col in range(min(b,d),max(b,d)+1)] +
                [(c, col) for col in range(min(b,d),max(b,d)+1)])
        inside = True
        for point in boundary:
            if point in inside_dict.keys():
                if inside_dict[point]:
                    continue
                else:
                    inside = False
                    break
            else:
                if is_inside(coords, point):
                    inside_dict[point] = True
                else:
                    inside_dict[point] = False
                    inside = False
                    break
        if inside:
            print(f'Rectangle with diagonal tiles {(a,b)} and {(c,d)} is inside. Area = {area}.')
            out = area

# out = 0
toc = time()
print(f'{toc-tic:.6f} secs: {out}')