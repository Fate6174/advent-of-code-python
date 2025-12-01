from utils.api import get_input

input_str = get_input(8)

# WRITE YOUR SOLUTION HERE
# collect frequency positions
lines = input_str.splitlines()
m, n = len(lines), len(lines[0])
frequencies = {}
for i in range(m):
    for j in range(n):
        if (c := lines[i][j]) != '.':
            if c in frequencies.keys():
                frequencies[c].append((i,j))
            else:
                frequencies[c] = [(i,j)]

# part 1
antinode_positions = set()
for frequency in frequencies.keys():
    nodes = frequencies[frequency]
    num_nodes = len(nodes)
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            row1, col1 = nodes[i]
            row2, col2 = nodes[j]
            row3, col3 = row1 - (row2 - row1), col1 - (col2 - col1)
            row4, col4 = row2 + (row2 - row1), col2 + (col2 - col1)
            for row, col in [(row3, col3), (row4, col4)]:
                if row >= 0 and row < m and col >= 0 and col < n:
                    antinode_positions.add((row, col))

print(f'part 1: {len(antinode_positions)}')

# part 2
antinode_positions = set()
for frequency in frequencies.keys():
    nodes = frequencies[frequency]
    num_nodes = len(nodes)
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            row1, col1 = nodes[i]
            row2, col2 = nodes[j]
            rowx, colx = row1, col1
            while rowx >= 0 and rowx < m and colx >= 0 and colx < n:
                antinode_positions.add((rowx, colx))
                rowx = rowx - (row2 - row1)
                colx = colx - (col2 - col1)
            rowx, colx = row2, col2
            while rowx >= 0 and rowx < m and colx >= 0 and colx < n:
                antinode_positions.add((rowx, colx))
                rowx = rowx + (row2 - row1)
                colx = colx + (col2 - col1)

print(f'part 2: {len(antinode_positions)}')