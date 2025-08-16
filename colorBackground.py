

import cv2
import numpy as np

image = np.zeros((200, 200, 3), np.uint8)

image[:,:] = (0, 0, 128)

cv2.imshow("Color", image)
cv2.waitKey()
