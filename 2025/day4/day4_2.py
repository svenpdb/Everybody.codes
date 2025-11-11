

input = open("input4_2", "r").read().split()
input = [int(i) for i in input]

N_out = 10000000000000
N_in = int(input[-1] / input[0] * N_out + 1)
print(N_in)
