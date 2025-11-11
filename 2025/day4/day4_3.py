
with open("input4_3", "r") as f:
    lines = f.readlines()

initial = int(lines[0])
final = int(lines[-1])
lines = lines[1:-1]

num = 1
denom = 1
for line in lines:
    line = [int(x) for x in line.split("|")]
    num *= line[1]
    denom *= line[0]

N_out = int(100 * num / denom * initial / final)
print(N_out)
