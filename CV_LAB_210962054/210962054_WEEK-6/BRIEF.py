'''pip install opencv-python==3.4.2.16
pip install opencv-contrib-python==3.4.2.16'''
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('C:/Users/PG LAB/Desktop/sample.jpg', cv.IMREAD_GRAYSCALE)
# Initiate FAST detector
star = cv.xfeatures2d.StarDetector_create()
# Initiate BRIEF extractor
brief = cv.xfeatures2d.BriefDescriptorExtractor_create()
# find the keypoints with STAR
kp = star.detect(img,None)
brief_image = cv.drawKeypoints(img, kp, img)
# compute the descriptors with BRIEF
kp, des = brief.compute(img, kp)
print( brief.descriptorSize() )
print( des.shape )
cv.imshow('image', brief_image)
# save the image
cv.imwrite("table-brief.jpg", brief_image)
cv.waitKey(0)
cv.destroyAllWindows()