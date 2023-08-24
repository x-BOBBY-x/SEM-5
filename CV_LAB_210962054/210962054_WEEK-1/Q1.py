import cv2

image = cv2.imread('C:/Users/PG LAB/Desktop/sample.jpg',cv2.IMREAD_UNCHANGED)
b,g,r = (image[150,150])
print(b)
print(g)
print(r)