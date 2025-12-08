from utils.api import get_input
from time import time

input_str = get_input(8)
# input_str = """10
# 162,817,812
# 57,618,57
# 906,360,560
# 592,479,940
# 352,342,300
# 466,668,158
# 542,29,236
# 431,825,988
# 739,650,466
# 52,470,668
# 216,146,977
# 819,987,18
# 117,168,530
# 805,96,715
# 346,949,466
# 970,615,88
# 941,993,340
# 862,61,35
# 984,92,344
# 425,690,689
# """

# WRITE YOUR SOLUTION HERE

# part 1
tic = time()
# parse coordinates
# CAUTION: the puzzle input needs to be manually chnaged so that the number of
# intended connections is the first line of the input:
# Public test: num_connections == 10,
# Private test: num_connections == 1000.
num_connections = int(input_str.splitlines()[0])
coords = [tuple([int(x) for x in line.split(',')]) for line in input_str.splitlines()[1:]]
# compute pairwise distances and sort by them
distances = [((x1-x2)**2+(y1-y2)**2+(z1-z2)**2, idx1, idx2) for (idx1, (x1,y1,z1)) in enumerate(coords) for (idx2, (x2,y2,z2)) in enumerate(coords) if idx1 < idx2]
distances.sort(key=lambda tup: tup[0])
# at the start each coordinate is in their own circuit
junkbox_to_circuit_id = {idx: idx for idx, coord in enumerate(coords)}
circuit_id_to_junkboxes = {idx: set([idx]) for idx, coord in enumerate(coords)}
for (_, idx1, idx2) in distances[:num_connections]:
    circuit_id1 = junkbox_to_circuit_id[idx1]
    circuit_id2 = junkbox_to_circuit_id[idx2]
    if circuit_id1 == circuit_id2:
        continue
    circuit_union = circuit_id_to_junkboxes[circuit_id1].union(circuit_id_to_junkboxes[circuit_id2])
    for junkbox in circuit_union:
        junkbox_to_circuit_id[junkbox] = circuit_id1
    circuit_id_to_junkboxes.pop(circuit_id2)
    circuit_id_to_junkboxes[circuit_id1] = circuit_union
# sort per size of circuit
circuits = list(circuit_id_to_junkboxes.values())
circuits.sort(key=lambda s: len(s), reverse=True)
out = 1
for circuit in circuits[:3]:
    out *= len(circuit)
toc = time()
print(f'{toc-tic:.6f} secs: {out}')

# part 2
tic = time()
# parse coordinates
# CAUTION: the puzzle input needs to be manually chnaged so that the number of
# intended connections is the first line of the input:
# Public test: num_connections == 10,
# Private test: num_connections == 1000.
coords = [tuple([int(x) for x in line.split(',')]) for line in input_str.splitlines()[1:]]
# compute pairwise distances and sort by them
distances = [((x1-x2)**2+(y1-y2)**2+(z1-z2)**2, idx1, idx2) for (idx1, (x1,y1,z1)) in enumerate(coords) for (idx2, (x2,y2,z2)) in enumerate(coords) if idx1 < idx2]
distances.sort(key=lambda tup: tup[0])
# at the start each coordinate is in their own circuit
junkbox_to_circuit_id = {idx: idx for idx, coord in enumerate(coords)}
circuit_id_to_junkboxes = {idx: set([idx]) for idx, coord in enumerate(coords)}
for (_, idx1, idx2) in distances:
    circuit_id1 = junkbox_to_circuit_id[idx1]
    circuit_id2 = junkbox_to_circuit_id[idx2]
    if circuit_id1 == circuit_id2:
        continue
    circuit_union = circuit_id_to_junkboxes[circuit_id1].union(circuit_id_to_junkboxes[circuit_id2])
    for junkbox in circuit_union:
        junkbox_to_circuit_id[junkbox] = circuit_id1
    circuit_id_to_junkboxes.pop(circuit_id2)
    circuit_id_to_junkboxes[circuit_id1] = circuit_union
    if len(circuit_id_to_junkboxes.keys()) == 1:
        out = coords[idx1][0] * coords[idx2][0]
        break
toc = time()
print(f'{toc-tic:.6f} secs: {out}')