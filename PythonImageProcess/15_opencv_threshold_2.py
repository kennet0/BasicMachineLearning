import cv2
import matplotlib.pyplot as plt


address = 'PythonImageProcess/files/'
image =cv2.imread(address+'hand_writing_image.jpg', cv2.IMREAD_GRAYSCALE)

images = []
ret, thres1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
thres2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21,3)

images.append(image)
images.append(thres1)
images.append(thres2)

for i in images:
    plt.imshow(cv2.cvtColor(i, cv2.COLOR_GRAY2RGB))
    plt.show()

