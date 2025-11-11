with open("input2", "r") as f:
    lines = f.readlines()

dirs = lines[-1].strip().split(",")
names = lines[0].strip().split(",")

dirs = [int(dir.replace("R", "+").replace("L", "-")) for dir in dirs]

length = len(names)
pos = sum(dirs) % length

print(names[pos])
