import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread('C:/Users/PG LAB/Desktop/sample.jpg')

Gaussian=cv2.GaussianBlur(image,(7,7),0)

(fig, axs) = plt.subplots(nrows=1, ncols=2, figsize=(8, 8))
axs[0].imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
axs[0].set_title('Original IMAGE')
axs[1].imshow(cv2.cvtColor(Gaussian,cv2.COLOR_BGR2RGB))
axs[1].set_title('GAUSSIAN BLUR')
plt.show()