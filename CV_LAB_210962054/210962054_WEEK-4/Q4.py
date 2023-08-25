import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread('C:/Users/PG LAB/Desktop/sample.jpg',0)
Gaussian=cv2.GaussianBlur(image,(7,7),0)
Sobely=cv2.Sobel(Gaussian,cv2.CV_64F,0,1,5)
Sobelx=cv2.Sobel(Gaussian,cv2.CV_64F,1,0,5)
Sobelxy=cv2.Sobel(Gaussian,cv2.CV_64F,1,1,5)
laplace=cv2.Laplacian(Gaussian,cv2.CV_64F)
sobel=np.hypot(Sobelx,Sobely)
phase=cv2.phase(Sobelx,Sobely)
(fig, axs) = plt.subplots(nrows=1, ncols=3, figsize=(8, 8))
axs[0].imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
axs[0].set_title('Original IMAGE')
axs[1].imshow(sobel,cmap="gist_gray")
axs[1].set_title('Gradient')
axs[2].imshow(phase,cmap="gist_gray")
axs[2].set_title('Phase')
plt.show()
