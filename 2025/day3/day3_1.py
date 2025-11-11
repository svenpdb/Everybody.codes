line = open("input3_1", "r").read().strip().split(",")
line = [int(i) for i in line]

unique = set(line)
unique = list(unique)

tot = sum(unique) 
print(tot)
