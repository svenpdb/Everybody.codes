input = list(map(int, open("input16_2", "r").read().strip().split(",")))

L = len(input)
cmp = [0] * L
wall = input[:]
start = 1
res = list()
while wall != cmp:
    if wall[start - 1] >= 1:
        res.append(start)
        for i in range(L // start):
            wall[start + i * start - 1] -= 1
    start += 1
    print("walls:", wall)
    print("res:", res)

print(res)
prod = 1
for i in res:
    prod *= i
    
print(prod)