def add(a, b):
    c = [0, 0]
    c[0] = a[0] + b[0]
    c[1] = a[1] + b[1]
    return c

def mult(a,b):
    c = [0, 0]
    c[0] = a[0] * b[0] - a[1] * b[1]
    c[1] = a[0] * b[1] + a[1] * b[0]
    return c

def div(a, b):
    c = [0, 0]
    c[0] = int(a[0] / b[0])
    c[1] = int(a[1] / b[1])
    return c


A = [-21703,67997]
length = 1001

dx = 1
count = 0
for x in range(length):
    for y in range(length):
        stop = 0
        res = [0, 0]
        pos = add(A, [dx*x, dx* y] )
        for i in range(100):
            res = mult(res, res)
            res = div(res, [100000, 100000])
            res = add(res, pos)

            if abs(res[0]) > 1000000 or abs(res[1]) > 1000000:
                stop = 1
                break
        if stop == 1:
            continue

        count += 1

print(count)
