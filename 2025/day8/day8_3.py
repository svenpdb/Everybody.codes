with open("input8_3", "r") as f:
    input = f.read().strip().split(",")
input = [int(i) for i in input]

connections = dict()
strings = [[input[0], input[1]]]
prev = input[1]

for nail in input[2:]:
    strings.append([prev, nail])
    prev = nail

for i in range(1, len(set(input))+1):
    for j in range(i+1, len(set(input))+1):
        connections[(i, j)] = 0
        if [i, j] in strings or [j, i] in strings: connections[(i, j)] += 1

for string1 in list(connections.keys()):
    for string2 in strings:
        low = min(string1[0], string1[1])
        high = max(string1[0], string1[1])

        if low < string2[0] < high and not low <= string2[1] <= high:
            connections[(low, high)] += 1

        if low < string2[1] < high and not low <= string2[0] <= high:
            connections[(low, high)] += 1


print(max(connections.values()))
