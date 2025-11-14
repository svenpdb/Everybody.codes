
##Probably will optimize some time later.

with open("input9_3", "r") as f:
#with open("tmp2", "r") as f:
    input = f.readlines()
strings = [inp.strip().split(":")[1] for inp in input]

length = len(strings)
connections = []

for child in range(length):
    for par1 in range(length):
        for par2 in range(par1 + 1, length):
            if child == par1 or child == par2: continue
            for x, y, z in zip(strings[child], strings[par1], strings[par2]):
                if x not in [y, z]:
                    break
            else:
                connections.append({min(par1+1, par2+1), max(par1+1, par2+1), child+1})

length = len(connections)
largest = 0

for fam1 in range(length):
    family = connections[fam1]
    prev = family
    while True:
        for fam2 in range(length):
            tmp = family & connections[fam2]
            if tmp != set():
                family = family | connections[fam2]

        if family == prev:
            break
        prev = family

    if len(family) > largest:
        largest = len(family)
        largestfam = family
        
tot = 0
for i in largestfam:
   tot += i 
print(tot)
