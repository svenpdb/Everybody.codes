def add(name, rules, unique):
    last_letter = name[-1]
    if len(name) >= 11: return name
    if last_letter not in rules: return name

    for l in rules[last_letter]:
        if 7 <= len(name) + 1 <= 11: unique.add(name + l) 
        add(name + l, rules, unique)


with open("input7_3", "r") as f:
    lines = f.readlines()

names, rules = lines[0], lines[2:]
names = names.strip().split(",")
unique = set()
ruleset = dict()

for rule in rules:
    first, last = rule.split(">")
    first = first.strip()
    last = last.strip().split(",")
    ruleset[first] = last

for prefix in names:
    for id in range(len(prefix) - 1):
        this_letter = prefix[id]
        next_letter = prefix[id+1]
        if next_letter not in ruleset[this_letter]: 
            break
    else:    
        add(prefix, ruleset, unique)

print(len(unique))
