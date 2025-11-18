def step(pos, steps):
    if 0 <= pos[0] < nrows and 0 <= pos[1] < ncols:
        pass
    else:
        return 0

    if steps == Nrounds + 1: 
        return 0 

    pos_at_round[steps].add(pos)

    step((pos[0] + 2, pos[1] + 1), steps + 1)
    step((pos[0] + 2, pos[1] - 1), steps + 1)
    step((pos[0] - 2, pos[1] + 1), steps + 1)
    step((pos[0] - 2, pos[1] - 1), steps + 1)
    step((pos[0] + 1, pos[1] + 2), steps + 1)
    step((pos[0] + 1, pos[1] - 2), steps + 1)
    step((pos[0] - 1, pos[1] + 2), steps + 1)
    step((pos[0] - 1, pos[1] - 2), steps + 1)

#with open("input10_2", "r") as f:
with open("tmp", "r") as f:
    input = f.readlines()

input = [list(inp.strip()) for inp in input]
hideouts = [[x == "#" for x in row] for row in input]
sheep = [[x == "S" for x in row] for row in input]

nrows = len(input)
ncols = len(input[0])
Nrounds = 3
pos_at_round = []
for i in range(Nrounds+1):
    pos_at_round.append(set())

for i, row in enumerate(input):
    if "D" in row:
        pos = row.index("D")
        start = (i, pos)
        break


length = len(input)

step((i, pos), 0)

empty = [False] * ncols
total = 0 

for i in pos_at_round:
    print(len(i))
    print(i)

for timestep in range(1, Nrounds + 1):
    print(timestep)
    for x, y in pos_at_round[timestep]:
        if sheep[x][y] and not hideouts[x][y]:
            total += 1
            sheep[x][y] = False
    sheep.insert(0, empty)
    sheep.pop(-1)
    for x, y in pos_at_round[timestep]:
        if sheep[x][y] and not hideouts[x][y]:
            total += 1
            sheep[x][y] = False

