def step(pos, steps):
    if 0 <= pos[0] < nrows / 2 and 0 <= pos[1] < ncols / 2:
        pass
    else:
        return 0

    if steps == Nrounds + 1: 
        return 0 

    pos_at_round[steps].add(pos)
    pos_at_round[steps].add((nrows - 1 - pos[0], pos[1]))
    pos_at_round[steps].add((pos[0], ncols - 1 - pos[1]))
    pos_at_round[steps].add((nrows - 1 - pos[0], ncols - 1- pos[1]))

    step((pos[0] + 2, pos[1] + 1), steps + 1)
    step((pos[0] + 2, pos[1] - 1), steps + 1)
    step((pos[0] - 2, pos[1] + 1), steps + 1)
    step((pos[0] - 2, pos[1] - 1), steps + 1)
    step((pos[0] + 1, pos[1] + 2), steps + 1)
    step((pos[0] + 1, pos[1] - 2), steps + 1)
    step((pos[0] - 1, pos[1] + 2), steps + 1)
    step((pos[0] - 1, pos[1] - 2), steps + 1)


def next_step(pos):
    res = set()
    for px, py in pos:
        for r, c in [[2, 1], [-2, 1], [2, -1], [-2, -1], [1, 2], [1, -2], [-1, 2] ,[-1, -2]]:
            p0 = px + r
            p1 = py + c
            if 0 <= p0 < nrows and 0 <= p1 < ncols:
                res.add((p0, p1))
    return res


with open("input10_2", "r") as f:
#with open("tmp", "r") as f:
    input = f.readlines()

input = [list(inp.strip()) for inp in input]
hideouts = [[x == "#" for x in row] for row in input]
sheep = [[x == "S" for x in row] for row in input]

nrows = len(input)
ncols = len(input[0])
Nrounds = 20

for i, row in enumerate(input):
    if "D" in row:
        pos = row.index("D")
        start = (i, pos)
        break

pos_at_round = {start}
length = len(input)
empty = [False] * ncols
total = 0 

for timestep in range(1, Nrounds + 1):
    pos_at_round = next_step(pos_at_round)

    for x, y in pos_at_round:
        if sheep[x][y] and not hideouts[x][y]:
            total += 1
            sheep[x][y] = False
    sheep.insert(0, empty)
    sheep.pop(-1)

    for x, y in pos_at_round:
        if sheep[x][y] and not hideouts[x][y]:
            total += 1
            sheep[x][y] = False

print(total)
