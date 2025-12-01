from utils.api import get_input

input_str = get_input(4)

# WRITE YOUR SOLUTION HERE
input_matrix = input_str.splitlines()
m, n = len(input_matrix), len(input_matrix[0])

# part 1
res = 0
for i in range(m):
    for j in range(n):
        if input_matrix[i][j] == 'X':
            l = []
            if j > 2:
                l += [[input_matrix[i][j-idx_shift] for idx_shift in [1,2,3]]]
                if i > 2:
                    l += [[input_matrix[i-idx_shift][j-idx_shift] for idx_shift in [1,2,3]]]
                if i < m - 2 - 1:
                    l += [[input_matrix[i+idx_shift][j-idx_shift] for idx_shift in [1,2,3]]]
            if i > 2:
                l += [[input_matrix[i-idx_shift][j] for idx_shift in [1,2,3]]]
            if i < m - 2 - 1:
                l += [[input_matrix[i+idx_shift][j] for idx_shift in [1,2,3]]]
            if j < n - 2 - 1:
                l += [[input_matrix[i][j+idx_shift] for idx_shift in [1,2,3]]]
                if i > 2:
                    l += [[input_matrix[i-idx_shift][j+idx_shift] for idx_shift in [1,2,3]]]
                if i < m - 2 - 1:
                    l += [[input_matrix[i+idx_shift][j+idx_shift] for idx_shift in [1,2,3]]]
            res += sum([1 if ''.join(item) == 'MAS' else 0 for item in l])

print(f'part1: {res}')

# part 2
res = 0
for i in range(1,m-1):
    for j in range(1,n-1):
        if input_matrix[i][j] == 'A':
            l = [
                [input_matrix[i-idx_shift][j-idx_shift] for idx_shift in [-1,0,1]],
                [input_matrix[i+idx_shift][j-idx_shift] for idx_shift in [-1,0,1]]
            ]
            res += 1 if all([''.join(item) in ['MAS', 'SAM'] for item in l]) else 0

print(f'part2: {res}')