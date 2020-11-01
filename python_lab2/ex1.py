def fib(n):
    x = list()
    if (n < 0):
        return None
    if (n == 1):
        return [1]
    x.extend([1, 1])
    if n == 2:
        return x
    for i in range(2, n):
        val = x[-1] + x[-2]
        x.append(val)
    return x


print(fib(10))
