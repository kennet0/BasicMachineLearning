import cv2

address = 'PythonImageProcess/files/'
image =cv2.imread(address+'cat.jpg')

print(image.shape)
print(image.size)

# 이미지 numpy객체의 특정 픽셀을 가리킨다.
px = image[100,100]

#B, G, R 순서대로 출력됨
print(px)

# R 값만 출력
print(px[2])