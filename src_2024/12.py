from utils.api import get_input
import numpy as np

input_str = get_input(12)

# WRITE YOUR SOLUTION HERE
garden_map = np.array([[c for c in line] for line in input_str.splitlines()])
garden_info = np.empty(garden_map.shape, dtype='object')

id = 0
idxs = np.where(garden_info == None)
while idxs[0].shape[0] > 0:
    i, j = idxs[0][0], idxs[1][0]
    plant_type = garden_map[i,j]
    neighbors_of_same_plant_type = [(i,j)]
    while neighbors_of_same_plant_type != []:
        x,y = neighbors_of_same_plant_type[0]
        if garden_info[x,y] is None:
            neighbors_2 = [
                (p,q,d) for p,q,d in [(x-1,y,'N'), (x,y+1,'E'), (x+1,y,'S'), (x,y-1,'W')]
                    if p >= 0 and p < garden_map.shape[0] and
                    q >= 0 and q < garden_map.shape[1] and
                    garden_map[p,q] == plant_type
            ]
            fence_sides = [c for c in 'NESW' if c not in [d for p,q,d in neighbors_2]]
            num_new_fence_sides = 0
            if 'N' in fence_sides:
                if 'N' not in [side for p,q,d in neighbors_2 if d in 'EW' if garden_info[p,q] is not None for side in garden_info[p,q][1]]:
                    num_new_fence_sides += 1
            if 'S' in fence_sides:
                if 'S' not in [side for p,q,d in neighbors_2 if d in 'EW' if garden_info[p,q] is not None for side in garden_info[p,q][1]]:
                    num_new_fence_sides += 1
            if 'E' in fence_sides:
                if 'E' not in [side for p,q,d in neighbors_2 if d in 'SN' if garden_info[p,q] is not None for side in garden_info[p,q][1]]:
                    num_new_fence_sides += 1
            if 'W' in fence_sides:
                if 'W' not in [side for p,q,d in neighbors_2 if d in 'SN' if garden_info[p,q] is not None for side in garden_info[p,q][1]]:
                    num_new_fence_sides += 1
            garden_info[x,y] = (id, fence_sides, num_new_fence_sides, (x,y))
            neighbors_3 = [(p,q) for p,q,d in neighbors_2 if garden_info[p,q] is None]
            neighbors_of_same_plant_type += neighbors_3
        neighbors_of_same_plant_type = neighbors_of_same_plant_type[1:]
        neighbors_of_same_plant_type.sort()
    idxs = np.where(garden_info == None)
    id += 1

# part 1
res = 0
for i in range(id):
    region_list = [len(fence_sides) for id, fence_sides, num_new_fence_sides, _ in garden_info.flatten() if id == i]
    res += len(region_list) * sum(region_list)

print(f'part 1: {res}')

# part 2
res = 0
for i in range(id):
    region_list = [num_new_fence_sides for id, fence_sides, num_new_fence_sides, _ in garden_info.flatten() if id == i]
    res += len(region_list) * sum(region_list)

print(f'part 2: {res}')