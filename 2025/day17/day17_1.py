def check_flow(R, xv, yv, xc, yc):
    left = (xv - xc)**2 + (yv - yc)**2
    return left <= R**2

input = list(list(row) for row in open("input17_1", "r").read().strip().split())
# print(input)

for index, line in enumerate(input):
    if "@" in line:
        volcano = (index, line.index("@"))
        print("volcano: ", index, line.index("@"))
        break
    
    
lava = {volcano}
som = 0
maxR = 10
for step in range(maxR+1):
    for i in range(-step, step+1, 1):
        for j in range(-step, step+1, 1):
            x, y = volcano[0] + i, volcano[1] + j
            if (x, y) in lava:
                continue
            else:
                if check_flow(step, volcano[0], volcano[1], x, y):
                    lava.add((x, y))
                    som += int(input[y][x])
                    
    print(som)