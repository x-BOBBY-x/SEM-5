import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread('C:/Users/PG LAB/Desktop/pattern.jpg',0)
Gaussian=cv2.GaussianBlur(image,(7,7),0)
Sobely=cv2.Sobel(Gaussian,cv2.CV_64F,0,1,5)
Sobelx=cv2.Sobel(Gaussian,cv2.CV_64F,1,0,5)
Sobelxy=cv2.Sobel(Gaussian,cv2.CV_64F,1,1,5)
laplace=cv2.Laplacian(Gaussian,cv2.CV_64F)
im=np.array(image,float)
img=im+(im-Sobely)
img1=im+(im-Sobelx)
img2=im+(im-Sobelxy)
img3=im+(im-laplace)

(fig, axs) = plt.subplots(nrows=1, ncols=5, figsize=(7, 7))
axs[0].imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
axs[0].set_title('Original IMAGE')
axs[1].imshow(Sobelx)
axs[1].set_title('Sobel:x')
axs[2].imshow(Sobely)
axs[2].set_title('Sobel:y')
axs[3].imshow(Sobelxy)
axs[3].set_title('Sobel:xy')
axs[4].imshow(laplace)
axs[4].set_title('Laplacian')
plt.show()
(fig1, axs1) = plt.subplots(nrows=1, ncols=4, figsize=(7, 7))
axs1[0].imshow(img)
axs1[0].set_title('Sharp-Y')
axs1[1].imshow(img1)
axs1[1].set_title('Sharp-X')
axs1[2].imshow(img2)
axs1[2].set_title('Sharp-XY')
axs1[3].imshow(img3)
axs1[3].set_title('Sharp-LA')
plt.show()