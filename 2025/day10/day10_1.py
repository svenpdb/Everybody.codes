def step(pos, steps):
    seen.add((pos))
    if steps == 4: return 0  
    step((pos[0] + 2, pos[1] + 1), steps + 1)
    step((pos[0] + 2, pos[1] - 1), steps + 1)
    step((pos[0] - 2, pos[1] + 1), steps + 1)
    step((pos[0] - 2, pos[1] - 1), steps + 1)
    step((pos[0] + 1, pos[1] + 2), steps + 1)
    step((pos[0] + 1, pos[1] - 2), steps + 1)
    step((pos[0] - 1, pos[1] + 2), steps + 1)
    step((pos[0] - 1, pos[1] - 2), steps + 1)




with open("input10_1", "r") as f:
#with open("tmp", "r") as f:
    input = f.readlines()

input = [list(inp.strip()) for inp in input]

for i, row in enumerate(input):
    if "D" in row:
        pos = row.index("D")
        start = (i, pos)
        break


length = len(input)
seen = set()
seen2 = set()

step((i, pos), 0)

tot = 0 
for x, y in seen:
    if (x, y) == start: continue
    if input[x][y] == "S":
        tot += 1
print(tot)
