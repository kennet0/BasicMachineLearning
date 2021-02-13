import numpy as np

array = np.array([5,8,1,4,3])
array.sort()
print(array)
print(array[::-1])

#각 열을 기준으로 정렬
array2 = np.array([[5,8,3,9,54],[6,3,1,6,5]])
print(array2)
array2.sort(axis=0)
print(array2)

