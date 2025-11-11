

input = open("input4_1", "r").read().split()
input = [int(i) for i in input]

N_in = 2025
N_out = int(input[0] / input[-1] * N_in)

print(N_out)
