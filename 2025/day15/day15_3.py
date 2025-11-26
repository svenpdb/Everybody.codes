from collections import deque
input = open("input15_3", "r").read().strip().split(",")

currentdir = 1

walls = set()

x, y = 0, 0

for instruction in input:
    direction = instruction[0]
    distance = int(instruction[1:])
    match direction:
        case "L":
            currentdir = (currentdir + 1) % 4
        case "R":
            currentdir = (currentdir - 1) % 4
    match currentdir:
        case 0:
            for j in range(1, distance+1):
                walls.add((x+j, y))
            x += distance
        case 1:
            for j in range(1, distance+1):
                walls.add((x, y-j))
            y -= distance
        case 2:
            for j in range(1, distance+1):
                walls.add((x-j, y))
            x -= distance
        case 3:
            for j in range(1, distance+1):
                walls.add((x, y+j))
            y += distance
endx, endy = x, y
xmin = 0
xmax = 0
ymin = 0
ymax = 0
for i,j in walls:
    if i < xmin:
        xmin = i - 2
    if i > xmax:
        xmax = i + 2
    if j < ymin:
        ymin = j - 2
    if j > ymax:
        ymax = j + 2
        
run = True
queue = deque()
queue.append((1, 0, 0))
explored = set()

while run:
    if len(queue) < 1:
        break
    
    dist, x, y = queue.popleft()
    for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        xnew = x + i
        ynew = y + j
        if (xnew, ynew) in explored:
            continue
        explored.add((xnew, ynew))
        if (xnew, ynew) == (endx, endy): 
            print("found, distance = ", dist)
            run = False
            break
        if xmin <= xnew <= xmax and ymin <= ynew <= ymax and (xnew, ynew) not in walls:
            queue.append((dist + 1, xnew, ynew))
