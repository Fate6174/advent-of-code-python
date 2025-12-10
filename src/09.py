from utils.api import get_input
from time import time

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
for idx, (a,b) in enumerate(coords):
    for (c,d) in coords[idx+1:]:
        # rectangle A = [a,b] -> [c,b] -> [c,d] -> [a,d]
        area = (abs(a-c) + 1) * (abs(b-d) + 1)
        # only do tests if the area is larger than the current maximum
        if area <= out:
            continue
        # test if the other corners are inside
        if not is_inside(coords, (c,b)) or not is_inside(coords, (a,d)):
            continue
        # test if the rectangle sides cross any polygon edge
        inside = True
        for (u,v), (w, x) in zip(coords, coords[1:] + [coords[0]]):
            if u == w:
                if min(a,c) < u and u < max(a,c):
                    if min(b,d) >= min(v,x) and min(b,d) < max(v,x):
                        inside = False
                        break
                    if max(b,d) > min(v,x) and max(b,d) <= max(v,x):
                        inside = False
                        break
            elif v == x:
                if v > min(b,d) and v < max(b,d):
                    if min(a,c) >= min(u,w) and min(a,c) < max(u,w):
                        inside = False
                        break
                    if max(a,c) > min(u,w) and max(a,c) <= max(u,w):
                        inside = False
                        break
        if inside:
            out = area

# out = 0
toc = time()
print(f'{toc-tic:.6f} secs: {out}')