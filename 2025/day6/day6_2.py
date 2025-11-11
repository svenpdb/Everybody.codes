with open("input6_2", "r") as f:
    lines = f.read().strip()

input = list(lines)
total = 0

for i in range(len(input)):
    if input[i].islower():
        total += input[:i].count(input[i].upper())

print(total)


