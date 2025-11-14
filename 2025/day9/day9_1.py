with open("input9_1", "r") as f:
#with open("tmp", "r") as f:
    input = f.readlines()



l = []
for i, line in enumerate(input):
    _, data = line.strip().split(":")
    l.append(data)
print(l)

child = [1, 1, 1]

for i, j, k in zip(l[0], l[1], l[2]):
    print(i, j, k)
    if i not in [j, k]:
        child[0] = 0
    if j not in [i, k]:
        child[1] = 0
    if k not in [i, j]:
        child[2] = 0

p1 = 0
p2 = 0
for i, j, k in zip(l[0], l[1], l[2]):
    print(i, j, k)
    if i == k:
        p1 += 1
    if j == k:
        p2 += 1
print(p1 * p2)
