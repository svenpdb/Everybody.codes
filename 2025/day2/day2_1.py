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


A = [160, 50]

res = [0, 0]

for i in range(3):
    res = mult(res, res)
    res = div(res, [10, 10])
    res = add(res, A)

print(res)
