import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread('C:/Users/PG LAB/Desktop/OIP1.jpg')
orig = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# perform a naive attempt to find the (x, y) coordinates of
# the area of the image with the largest intensity value
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
cv2.circle(image, maxLoc, 10, (255, 0, 0), 2)
# display the results of the naive attempt
cv2.imshow("DETECTOR", image)
cv2.waitKey(0)