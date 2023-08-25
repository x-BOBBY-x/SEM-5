import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread('C:/Users/PG LAB/Desktop/sample.jpg',0)
can=cv2.Canny(image,140,140)
cv2.imshow("CANNY EDGE DETECTOR",can)
cv2.waitKey(0)