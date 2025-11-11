with open("input1", "r") as f:
    lines = f.readlines()

dirs = lines[-1].strip().split(",")
names = lines[0].strip().split(",")

dirs = [int(dir.replace("R", "+").replace("L", "-")) for dir in dirs]

length = len(names)
pos = 0

for dir in dirs:
    pos = pos + dir

    if pos > length - 1: 
        pos = length - 1
    if pos < 0:
        pos = 0

print(names[pos])
