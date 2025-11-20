input = list(map(str, open("input13_2", "r").read().strip().split()))

dial = [1]
inputright = input[::2]
for i in inputright:
    x, y = map(int, i.split("-"))
    tmp = [x + j for j in range(y - x + 1)]
    dial += tmp    
    
inputleft = input[1::2]
for i in inputleft[::-1]:
    x, y = map(int, i.split("-"))
    tmp = [y - j for j in range(y-x+1)]
    dial += tmp

turns = 20252025
length = len(dial)
pos = turns % length

print(dial[pos])
