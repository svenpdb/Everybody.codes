input = list(map(int, open("input16_3", "r").read().strip().split(",")))

L = len(input)
done = [0] * L
wall = input[:]
start = 1
res = list()
blocks = 202520252025000


while wall != done:
    if wall[start - 1] >= 1:
        res.append(start)
        for i in range(L // start):
            wall[start + i * start - 1] -= 1
    start += 1

n = len(res)

top = (blocks - n)
bottom = 0
for i in res:
    top *= i
    prod = 1
    for j in res:
        if i == j: continue
        prod *= j
    bottom += prod

approx = int(top / bottom - 1)

while True:
    som = 0
    for i in res:
        som += approx // i
    if som > blocks:
        print(approx - 1)
        break
    
    
    
    approx += 1