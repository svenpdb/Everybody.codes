with open("input6_3", "r") as f:
    lines = f.read().strip()

input = list(lines)

rangelim = 1000
N = 1000

length = len(input)


inputalt = input[:] * N
start = input + inputalt[:rangelim]
loop = inputalt[-rangelim:] + input + inputalt[:rangelim]
end = inputalt[-rangelim:] + input
total = 0

for i in range(0, length):
    j = i + rangelim
    if loop[j].islower():
        total += loop[j - rangelim:j+rangelim+1].count(loop[j].upper())
total = total * (N - 2)

for j in range(0, length):
    if start[j].islower():
        if j - rangelim < 0: 
            low = 0
        else:
            low = j - rangelim
        total += start[low:j+rangelim + 1].count(start[j].upper())

for i in range(0, length):
    j = i + rangelim
    if end[j].islower():
        if j > length + rangelim: 
            high = length + rangelim
        else:
            high = j + rangelim + 1
        total += end[j - rangelim:high].count(end[j].upper())

print(total)
