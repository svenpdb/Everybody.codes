with open("input3", "r") as f:
    lines = f.readlines()

dirs = lines[-1].strip().split(",")
names = lines[0].strip().split(",")

dirs = [int(dir.replace("R", "+").replace("L", "-")) for dir in dirs]

length = len(names)
for dir in dirs:
    names[0], names[dir%length] = names[dir%length], names[0]

print(names[0])
