def run_N_rounds(N, specificRound = 1):
    remainder = 0
    input = [[0] * L] * L
    boardsave = [i[:] for i in input]
    tot = 0

    for round in range(Nrounds):
        if round == 1:
            boardsave = [p[:] for p in nextround]

        nextround = [i[:] for i in input]
        for c in range(Lhalf):
            for r in range(Lhalf):
                som = 1
                for p, q in [(0, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    x = c + p
                    y = r + q
                    if (0 <= x < L and 0 <= y < L) == False:
                        continue
                
                    som += input[x][y]
                nextround[c][r] = som % 2
                nextround[L-c-1][L-r-1] = som % 2
                nextround[c][L-r-1] = som % 2
                nextround[L-c-1][r] = som % 2

        equal = True 
        for column in range(ncols):
            for row in range(nrows):
                if nextround[13 + column][13 + row] != pattern[column][row]:
                    equal = False
                    break
            if equal == False:
                break

        if equal:
            tmp = 0
            for row in nextround:
                tmp += sum(row)
            tot += tmp
        
        if round == specificRound:
            remainder = tot

        if round > 1 and boardsave == input:
            cyclesize = round - 1
            return cyclesize, tot, remainder

        input = nextround

    return 0, tot, remainder




pattern = list(map(list, open("input14_3", "r").read().strip().split()))
pattern = [[int(el == "#") for el in row] for row in pattern]

ncols = len(pattern)
nrows = len(pattern[0])
Nrounds = 1000000000

L = 34
Lhalf = int(L / 2)

cyclesize, tot, _ = run_N_rounds(Nrounds)

Ncycles = Nrounds // cyclesize
_, _, remainder = run_N_rounds(cyclesize, Nrounds % cyclesize)

res = tot * Ncycles + remainder
print(tot, Ncycles, remainder)
print(res)
