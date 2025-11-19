from collections import deque

def fill(pos, inp):
    visited = set()
    
    tocheck = deque()
    tocheck.append(pos)
    run = True

    while run:
        if len(tocheck) == 0: return len(visited), visited
        newpos = tocheck.popleft()
        if newpos in visited: 
            continue
        else:
            visited.add(newpos)

        for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x = newpos[0] + i
            y = newpos[1] + j
            if 0 <= x < cols and 0 <= y < rows:
                pass
            else:
                continue
            if inp[x][y] > inp[newpos[0]][newpos[1]] or inp[x][y] == -1:  continue
            tocheck.append((x, y)) 

def find_best_position(inp):
    best = 0

    for c in range(cols):
        for r in range(rows):
            tot, seen = fill((c, r), inp)
            if tot > best:
                best = tot
                bestset = seen
                bestpos = (c, r)

    return bestpos, bestset


def modify_input(inp, exploded):

    for r in range(rows):
        for c in range(cols):
            if (c, r) in exploded:
                inp[c][r] = -1
    return inp




input = list(map(list, [[int(x) for x in r] for r in open("input12_3", "r").read().strip().split()]))

cols = len(input)
rows = len(input[0])
startpositions = list()

inp = [x[:] for x in input]
for n in range(3):
    bestpos, exploded = find_best_position(inp)
    startpositions.append(bestpos)
    
    inp = modify_input(inp, exploded)


totexplosions = set()
for n in range(3):
    tot, exploded = fill(startpositions[n], input)
    totexplosions |= exploded

print(len(totexplosions))
