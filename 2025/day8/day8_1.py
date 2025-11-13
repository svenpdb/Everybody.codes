with open("input8_1", "r") as f:
    input = f.read().strip().split(",")
input = [int(i) for i in input]

length = max(input)

shift = input[1:] + [0]
diff = [abs(i - j) for i, j in zip(shift, input)]
print(diff.count(length / 2))
