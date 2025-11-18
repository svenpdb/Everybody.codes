def next_step(pos):
    res = set()
    for px, py in pos:
        for r, c in [[2, 1], [-2, 1], [2, -1], [-2, -1], [1, 2], [1, -2], [-1, 2] ,[-1, -2]]:
            p0 = px + r
            p1 = py + c
            if 0 <= p0 < nrows and 0 <= p1 < ncols:
                res.add((p0, p1))
    return res



with open("input10_1", "r") as f:
#with open("tmp", "r") as f:
    input = f.readlines()

input = [list(inp.strip()) for inp in input]
nrows = len(input)
ncols = len(input[0])
Nrounds = 10

for i, row in enumerate(input):
    if "D" in row:
        pos = row.index("D")
        start = (i, pos)
        break

length = len(input)

positions = {start}
for istep in range(Nrounds):
    tmp = next_step(positions)
    positions = positions | next_step(positions)

tot = 0
for x, y in positions:
    if (x, y) == start: continue
    if input[x][y] == "S":
        tot += 1
print(tot)
