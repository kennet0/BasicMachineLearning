import cv2
import numpy as np
import matplotlib.pyplot as plt

address = 'PythonImageProcess/files/'
image =cv2.imread(address+'gray_image.jpg')

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

# size = 4
# kernel = np.ones((size, size), np.float32) / (size ** 2)
# print(kernel)

# dst = cv2.filter2D(image, -1, kernel)
dst = cv2.blur(image,(4,4))
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.show()

