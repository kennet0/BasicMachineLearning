import cv2
import matplotlib.pyplot as plt

address = 'PythonImageProcess/files/'
image =cv2.imread(address+'cat.jpg')

# numpy slicing : ROI 처리 가능
roi = image[200:350, 50:200]

image[0:150, 0:150] = roi



plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()
