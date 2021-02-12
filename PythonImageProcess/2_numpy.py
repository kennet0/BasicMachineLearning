import numpy as np

#array 합치기
array1 = np.arange(4)
array2 = np.arange((5))

arrayadd = np.concatenate([array1,array2])
print(arrayadd.shape)
print(arrayadd)

#array 저장 및 불러오기
np.save('PythonImageProcess/saved.npy', arrayadd)
result = np.load('PythonImageProcess/saved.npy')
print(result)

#복수 어레이 저장 및 불러오기
np.savez('PythonImageProcess/saveAll.npz', array1=array1, array2=array2)
data = np.load('PythonImageProcess/saveAll.npz')

result1 = data['array1']
result2 = data['array2']
print(result1)
print(result2)
