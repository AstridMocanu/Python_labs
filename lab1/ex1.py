'''The greatest common divisor of multiple numbers read from the console.'''

def gcd(a, b):
    (a, b) = (max(a, b), min(a, b))

    while b:
        (q, r) = divmod(a, b)
        (a, b) = (b, r)

    return a


def mgcd():
    n = input()
    n=int(n)
    x = input()
    x=int(x)
    cmmdc = x
    for i in range(1, n ):
        y = input()
        y=int(y)
        cmmdc = gcd(cmmdc, y)
    return cmmdc

print(mgcd())