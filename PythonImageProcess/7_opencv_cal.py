import cv2
import matplotlib.pyplot as plt
import time

address = 'PythonImageProcess/files/'
image =cv2.imread(address+'cat.jpg')

start_time = time.time()

for i in range(0,100):
    for j in range(0,100):
        image[i, j] = [255,255,255]
print("--- %s seconds ---" %(time.time() - start_time))

start_time = time.time()
image[0:100, 0:100] = [0 ,0 ,0]
print("--- %s seconds ---" %(time.time() - start_time))

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

