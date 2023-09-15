import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('C:/Users/PG LAB/Desktop/1.jpg')
cv2.imshow('ORiginal TEST CASE-1', img)

img=cv2.GaussianBlur(img,(7,7),0)

img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)

img=cv2.add(img,thresh4)

img=img1+(img-thresh4)
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


#cv2.imshow('Set to 0', thresh4)


#ret, thresh = cv.threshold(img2, 127, 255, cv.THRESH_BINARY)
#th2 = cv.adaptiveThreshold(img2, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY, 11, 2)
cv2.imshow('TEST CASE-1', img1)
#CASE_2




img = cv2.imread('C:/Users/PG LAB/Desktop/3.jpg')
#cv2.imshow('ORiginal TEST CASE-2', img)
img=cv2.GaussianBlur(img,(7,7),0)
#cv2.imshow('gaussian', img)
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
ret, thresh4 = cv2.threshold(img1, 100, 255, cv2.THRESH_TOZERO_INV)

img=cv2.add(img,thresh4)

img=img+(img1-thresh4)
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#cv2.imshow('Set to 0', thresh4)
#ret, thresh = cv.threshold(img2, 127, 255, cv.THRESH_BINARY)
#th2 = cv.adaptiveThreshold(img2, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY, 11, 2)
#cv2.imshow('TEST CASE-2', img1)






img = cv2.imread('C:/Users/PG LAB/Desktop/2.jpg')
cv2.imshow('ORiginal TEST CASE-3', img)
img=cv2.GaussianBlur(img,(7,7),0)
#cv2.imshow('gaussian', img)
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
ret, thresh4 = cv2.threshold(img, 10, 255, cv2.THRESH_TOZERO)

img=cv2.add(img,thresh4)
img=img1+(img-thresh4)
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


#cv2.imshow('Set to 0', thresh4)


#ret, thresh = cv.threshold(img2, 127, 255, cv.THRESH_BINARY)
#th2 = cv.adaptiveThreshold(img2, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY, 11, 2)
cv2.imshow('TEST CASE-3', img1)
(fig, axs) = plt.subplots(nrows=3, ncols=3, figsize=(8, 8))
cv2.waitKey(0)
