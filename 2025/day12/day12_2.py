

def fill(pos):
    if pos in seen: return
    seen.add(pos)
    global tot
    tot += 1
    for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        x = pos[0] + i
        y = pos[1] + j
        if 0 <= x < cols and 0 <= y < rows:
            pass
        else:
            continue
        if input[x][y] > input[pos[0]][pos[1]]: continue
        fill((x, y))



input = list(map(list, [[int(x) for x in r] for r in open("input12_2", "r").read().strip().split()]))
#input = list(map(list, [[int(x) for x in r] for r in open("tmp", "r").read().strip().split()]))


for x in input: print(x)

cols = len(input)
rows = len(input[0])
print(cols, rows)

seen = set()
tot = 0

fill((0, 0))
print(len(seen))
fill((cols-1, rows-1))

print(len(seen))
print(tot)
