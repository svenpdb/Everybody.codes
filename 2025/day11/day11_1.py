input = list(map(int, (open("input11_1", "r").read().strip().split())))
change = True
count = 0
max = 10
length = len(input)

while change:
    change = False
    for i in range(length - 1):
        if input[i] > input[i+1]:
            input[i] -= 1
            input[i + 1] += 1
            change = True
    if count == max:
        break
    count += 1

change = True

while change:
    change = False
    for i in range(length - 1):
        if input[i] < input[i+1]:
            input[i] += 1
            input[i + 1] -= 1
            change = True
            
    if count == max:
        break
    count += 1


total = 0
for i in range(len(input)):
    total += (i+1) * input[i]

print(total)
