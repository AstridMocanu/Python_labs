import numpy as np

def is_prim(x):

    if x<2 :
        return 0
    if x==2:
        return 1

    if x%2==0:
        return 0

    for i in range(3,x):
        for j in range(i*i,x-1,2*i):
            if i%j==0:
                return 0
    return 1

print(is_prim(10))
print(is_prim(47))


