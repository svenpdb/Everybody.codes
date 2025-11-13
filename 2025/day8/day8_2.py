with open("input8_2", "r") as f:
    input = f.read().strip().split(",")
input = [int(i) for i in input]

count = 0
strings = [[input[0], input[1]]]
prev = input[1]
for nail in input[2:]:
    for string in strings[:-1]:
        low = min(string[0], string[1])
        high = max(string[0], string[1])


        if low < prev < high and not low <= nail <= high:
            count += 1
        if low < nail < high and not low <= prev <= high:
            count += 1

    strings.append([prev, nail])
    prev = nail
    
print(count)
