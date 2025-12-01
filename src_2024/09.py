from utils.api import get_input

input_str = """2333133121414131402"""
input_str = get_input(9)

# WRITE YOUR SOLUTION HERE

# part 1
block_info = []
free_info = []
idx = 0
for k, c in enumerate(input_str):
    if k % 2 == 0:
        block_info.append((idx, idx + int(c), k // 2))
    else:
        free_info.append((idx, idx + int(c)))
    idx += int(c)

res = 0
idx = 0
while block_info != []:
    block_a, block_b, block_id = block_info[0]
    while block_b > block_a:
        res += idx*block_id
        idx += 1
        block_b -= 1
    block_info = block_info[1:]
    
    if free_info == []:
        break
    free_a, free_b = free_info[0]
    if block_info == []:
        break
    block_a, block_b, block_id = block_info[-1]
    
    while free_b > free_a:
        if block_b > block_a:
            res += idx*block_id
            idx += 1
            free_b -= 1
            block_b -= 1
        else:
            block_info = block_info[:-1]
            if block_info == []:
                break
            block_a, block_b, block_id = block_info[-1]
    if block_info == []:
        break
    block_info[-1] = (block_a, block_b, block_id)
    free_info = free_info[1:]

print(f'part 1: {res}')

# part 2
block_info = []
free_info = []
idx = 0
for k, c in enumerate(input_str):
    if k % 2 == 0:
        block_info.append((idx, idx + int(c), k // 2))
    else:
        free_info.append((idx, idx + int(c)))
    idx += int(c)

for i in range(len(block_info)-1, 0, -1):
    block_a, block_b, block_id = block_info[i]
    for j in range(i):
        free_a, free_b = free_info[j]
        if free_b - free_a >= block_b - block_a:
            block_info[i] = (free_a, free_a + block_b - block_a, block_id)
            free_info[j] = (free_a + block_b - block_a, free_b)
            break

res = sum([idx * block_id for block_a, block_b, block_id in block_info for idx in range(block_a, block_b)])

print(f'part 2: {res}')