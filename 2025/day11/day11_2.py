input = list(map(int, (open("input11_2", "r").read().strip().split())))
change = True
count = 0
max = 10
while change:
    count += 1
    change = False
    for i in range(len(input) - 1):
        if input[i] > input[i+1]:
            input[i] -= 1
            input[i + 1] += 1
            change = True
    if change == False:
        count -= 1

change = True
while change:
    count += 1
    change = False
    for i in range(len(input) - 1):
        if input[i] < input[i+1]:
            input[i] += 1
            input[i + 1] -= 1
            change = True
            
    if change == False:
        count -= 1
            

print(count)
