with open("input7_1", "r") as f:
    lines = f.readlines()

names, rules = lines[0], lines[2:]
names = names.split(",")

for name in names:
    stop = 0
    for rule in rules:
        first, last = rule.split(">")
        first = first.strip()
        last = last.strip().split(",")
        if name.find(first) == -1:
            continue

        firstpos = name.find(first)
        if firstpos == len(name)-1: continue
        next = name[firstpos+1]

        if next not in last:
            break
    else:
        print(name)
