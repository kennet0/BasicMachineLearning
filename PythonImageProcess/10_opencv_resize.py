from PIL.Image import NONE
import cv2

address = 'PythonImageProcess/files/'
image =cv2.imread(address+'cat.jpg')

cv2.imshow('image1' ,image)
cv2.waitKey(0)

expand = cv2.resize(image, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)
cv2.imshow('image2' ,expand)
cv2.waitKey(0)

shrink = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
cv2.imshow('image3' ,shrink)
cv2.waitKey(0)