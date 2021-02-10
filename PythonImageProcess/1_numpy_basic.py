import numpy as np

array1 = np.arange(4)
print(array1)

array2 = np.zeros((4,4), dtype=float)
print(array2)

array3 = np.ones((4,4), dtype=float)
print(array3)

array4 = np.random.randint(0, 10, (3,3))
print(array4)

array5 = np.random.normal(0, 1,(3,3))
print(array5)

