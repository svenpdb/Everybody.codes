input = list(map(int, (open("input11_2", "r").read().strip().split())))

change = True
count = 0
length = len(input)

while change:
    count += 1
    change = False
    for i in range(length - 1):
        if input[i] > input[i+1]:
            input[i] -= 1
            input[i + 1] += 1
            change = True
    if change == False:
        count -= 1

av = int(sum(input) / length)

for i in range(length):
    if input[i] > av: break
    count += av - input[i]

print(count)
exit(0)
