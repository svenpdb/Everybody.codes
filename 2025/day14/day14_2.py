
input = list(map(list, open("input14_2", "r").read().strip().split()))
input = [[int(el == "#") for el in row] for row in input]

for i in input: print(i)

ncols = len(input)
nrows = len(input[0])
Nrounds = 2025

tot = 0
for round in range(Nrounds):
    nextround = [i[:] for i in input]
    for c in range(ncols):
        for r in range(nrows):
            som = 1
            for p, q in [(0, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                x = c + p
                y = r + q
                if (0 <= x < ncols and 0 <= y < nrows) == False:
                    continue
                
                som += input[x][y]
            nextround[c][r] = som % 2
    
    for row in nextround:
        tot += sum(row)
    input = nextround
print(tot)
