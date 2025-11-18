def next_step(pos):
    res = set()
    for px, py in pos:
        for r, c in [[2, 1], [-2, 1], [2, -1], [-2, -1], [1, 2], [1, -2], [-1, 2] ,[-1, -2]]:
            p0 = px + r
            p1 = py + c
            if 0 <= p0 < nrows and 0 <= p1 < ncols:
                res.add((p0, p1))
    return res


#with open("input10_3", "r") as f:
with open("tmp", "r") as f:
    input = f.readlines()

input = [list(inp.strip()) for inp in input]
hideouts = [[x == "#" for x in row] for row in input]
sheep = [[x == "S" for x in row] for row in input]

nrows = len(input)
ncols = len(input[0])
Nsheep = sum(sheep[0])
print(Nsheep)
Nrounds = (nrows + 1) * ncols
Nrounds =  10
sheep.append([False] * ncols)

sheep_steps = []
sh_list = [i for i in range(Nsheep)]
sheep_steps = [[i] for i in range(Nsheep)]

sheep_steps = [[]] * Nrounds**Nsheep
print(sheep_steps)



print("Sheep:")
for r in sheep: print(r)
print("=" * 20)
print("hideouts:")
for r in hideouts: print(r)


for i, row in enumerate(input):
    if "D" in row:
        pos = row.index("D")
        start = (i, pos)
        break

pos_at_round = {start}
length = len(input)
empty = [False] * ncols
total = 0 
run = True


