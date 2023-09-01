import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('C:/Users/PG LAB/Desktop/sample.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('Original',img)
cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
low_threshold = 50
high_threshold = 100
edges = cv2.Canny(gray, low_threshold, high_threshold)
cv2.imshow('Canny Edge detected image',edges)
cv2.waitKey(0)

rho = 1
theta = np.pi/180
threshold = 10
min_line_length = 50
max_line_gap = 5

line_image = np.copy(img)

lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)

for line in lines:
    for x1, y1, x2, y2 in line:
        cv2.line(line_image,(x1,y1), (x2,y2), (255,0,0), 2)

cv2.imshow('Hough Edge Detected',line_image)
cv2.waitKey(0)
cv2.destroyAllWindows()