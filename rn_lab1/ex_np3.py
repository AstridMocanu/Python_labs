import numpy as np

a=np.random.random((5,5))

print(a)
print(a.T)
print(np.linalg.inv(a))
print(np.linalg.det(a))
print(np.eye(2))