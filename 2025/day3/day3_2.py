line = open("input3_2", "r").read().strip().split(",")
line = [int(i) for i in line]

unique = set(line)
unique = list(unique)

unique.sort()
unique = unique[:20]
print(sum(unique))
