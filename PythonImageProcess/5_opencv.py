import cv2

address = 'PythonImageProcess/files/'
img_basic = cv2.imread(address+'cat.jpg', cv2.IMREAD_COLOR)
cv2.imshow('Image Basic',img_basic)
cv2.waitKey(0)
cv2.imwrite(address+'result1.png', img_basic)

img_gray = cv2.cvtColor(img_basic, cv2.COLOR_BGR2GRAY)
cv2.imshow('Image Basic',img_gray)
cv2.waitKey(0)