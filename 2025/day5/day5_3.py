import functools

def keyfunc(a,b):
    if a > b:
        return -1
    if b > a: return 1
    return 0

data = open("input5_3", "r").readlines()

min = 1e10
max = 0

info = []

for input in data:
    identity, input = input.split(":")
    input = input.strip().split(",")
    qual = input[0]
    spine = [["", input[0], ""]]
    levels = []

    for num in input[1:]:
        stop = 0
        for seg in range(len(spine)):
            if int(num) < int(spine[seg][1]) and spine[seg][0] == "":
                spine[seg][0] = num
                stop = 1
                break

            if int(num) > int(spine[seg][1]) and spine[seg][2] == "":
                spine[seg][2] = num
                stop = 1
                break

        if stop == 1:
            continue

        spine += [["", num, ""]]
        qual += num
    
    for seg in range(len(spine)):
        tmp = "".join(spine[seg])
        levels += [int(tmp)]

    if int(qual) < min:
        min = int(qual)

    if int(qual) > max:
        max = int(qual)

    info += [[int(qual), levels, int(identity)]]


a = sorted(info, key=functools.cmp_to_key(keyfunc))

checksum = 0

for index, ii in enumerate(a):
    checksum += (index + 1) * ii[2]

print(checksum)
