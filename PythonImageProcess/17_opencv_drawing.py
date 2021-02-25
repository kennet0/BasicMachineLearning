import cv2
import numpy as np
import matplotlib.pyplot as plt

image = np.full((512,512,3), 255, np.uint8)

# draw line
# image = cv2.line(image, (0,0), (255,255), (255,0,0),3)

# draw rectangle
# image = cv2.rectangle(image, (20,20), (255,255), (255,0,0),3)

# draw circle
# image = cv2.circle(image, (255,255), 100, (255,0,0), 3)

# draw polyline
# points = np.array([[5,5], [128,258], [483,444], [400, 150]])
# image = cv2.polylines(image,[points], True, (0,0,255), 4 )

# draw text
image = cv2.putText(image, 'Hello World', (0,200), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (255,0,0))

plt.imshow(image)
plt.show()