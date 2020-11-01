import numpy as np

a=np.random.random(7)
b=np.random.random(7)

print(a.dot(b))
s=0
for i in a:
    s=s+i

ss=0
for i in b:
    ss=ss+i

print(s>ss)

print(np.sqrt(a))