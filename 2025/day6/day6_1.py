with open("input6_1", "r") as f:
    lines = f.read().strip()

input = list(lines)

Acount = 0
total = 0

for i in input:
    if i == "A":
        Acount += 1
    if i == "a":
        total += Acount

print(total)
