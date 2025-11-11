import numpy as np
line = open("input3_3", "r").read().strip().split(",")
line = [int(i) for i in line]

line.sort(reverse=True)

line = np.array(line)
filt = np.ones(len(line))
sets = 0

while len(line) != 0:
    prev = 1e20
    for index, box in enumerate(line):
        if box < prev:
            filt[index] = 0
        prev = box


    line = line[filt == 1]
    filt = np.ones(len(line))
    sets += 1
print(sets)
