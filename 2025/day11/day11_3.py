input = list(map(int, (open("input11_3", "r").read().strip().split())))

count = 0
length = len(input)
av = int(sum(input) / length)

for i in range(length):
    if input[i] > av: break
    count += av - input[i]

print(count)
