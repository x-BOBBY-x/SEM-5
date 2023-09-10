import cv2 as cv
import numpy as np




img = cv.imread('C:/Users/PG LAB/Desktop/sample.jpg')

lower = np.array([10, 0, 210], dtype=np.uint8)
upper = np.array([160, 40, 255], dtype=np.uint8)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv, lower, upper)
output = cv.bitwise_and(img, img, mask=mask)
output = cv.dilate(output, (5, 5), iterations=5)

    # Display output image
cv.imshow('image', output)
cv.waitKey(0)

