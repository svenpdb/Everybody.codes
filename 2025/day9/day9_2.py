with open("input9_2", "r") as f:
#with open("tmp", "r") as f:
    input = f.readlines()



strings = []
for i, line in enumerate(input):
    _, data = line.strip().split(":")
    strings.append(data)
length = len(strings)
total = 0
print(length)
for child in range(length):
    for par1 in range(length):
        for par2 in range(par1 + 1, length):
            if child == par1 or child == par2: continue
            p1 = 0
            p2 = 0
            for x, y, z in zip(strings[child], strings[par1], strings[par2]):
                if x not in [y, z]:
                    break

                if x == y:
                    p1 += 1
                if x == z:
                    p2 += 1

            else:
                total += p1 * p2
                print(child, par1, par2, p1, p2,  p1 * p2)
print(total)
