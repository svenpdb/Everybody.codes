input = list(map(int, open("input16_1", "r").read().strip().split(",")))

L = 90

wall = [0] * 90

som = 0

for i in input:
    som += 90 // i
print(som)
print(input)