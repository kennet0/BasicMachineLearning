import cv2
import numpy as np
import matplotlib.pyplot as plt

address = 'PythonImageProcess/files/'
image =cv2.imread(address+'cat.jpg')

height, width = image.shape[:2]

M = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 0.5)
print(M)
dst = cv2.warpAffine(image, M ,(width, height))

plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.show()