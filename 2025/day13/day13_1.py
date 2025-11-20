input = list(map(int, open("input13_1", "r").read().strip().split()))
dial = [1] + input[::2] + input[1::2][::-1]

turns = 2025
length = len(dial)
pos = turns % length


print(dial[pos])