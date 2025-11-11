input = open("input5_1", "r").read()
identity, input = input.split(":")
input = input.strip().split(",")

qual = input[0]
spine = [["", input[0], ""]]

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
        
print(qual)
