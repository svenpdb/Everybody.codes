input = list(map(int, (open("input11_1", "r").read().strip().split())))
change = True
count = 0
max = 11
while change:
    count += 1
    change = False
    for i in range(len(input) - 1):
        if input[i] > input[i+1]:
            input[i] -= 1
            input[i + 1] += 1
            change = True
    if count == max:
        break

change = True
print(input)
while change:
    count += 1
    change = False
    for i in range(len(input) - 1):
        if input[i] < input[i+1]:
            input[i] += 1
            input[i + 1] -= 1
            change = True
            
    if count == max:
        break
print(input)
total = 0
for i in range(len(input)):
    total += (i+1) * input[i]
print(total)