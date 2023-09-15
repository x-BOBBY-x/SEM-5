import cv2
import numpy as np
img = cv2.imread('C:/Users/PG LAB/Desktop/R.jpg', cv2.IMREAD_GRAYSCALE)
surf = cv2.xfeatures2d.SURF_create()
keypoints_surf, descriptors = surf.detectAndCompute(img, None)
img2 = cv2.drawKeypoints(img, keypoints_surf, img, color=(100,25,20), flags=4)
cv2.imshow("SURF_IMAGE",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()