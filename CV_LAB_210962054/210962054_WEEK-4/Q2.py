import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread('C:/Users/PG LAB/Desktop/sample.jpg')
Gaussian=cv2.GaussianBlur(image,(7,7),0)
img=cv2.subtract(image,Gaussian)
img1=cv2.add(image,img)
(fig, axs) = plt.subplots(nrows=1, ncols=3, figsize=(8, 8))
axs[0].imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
axs[0].set_title('Original IMAGE')
axs[1].imshow(cv2.cvtColor(Gaussian,cv2.COLOR_BGR2RGB))
axs[1].set_title('GAUSSIAN BLUR')
axs[2].imshow(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
axs[2].set_title('GAUSSIAN SHARPENING')
plt.show()