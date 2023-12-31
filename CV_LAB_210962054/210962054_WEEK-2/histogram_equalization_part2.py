import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('C:/Users/PG LAB/Desktop/sample.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
equalized=cv2.equalizeHist(img)
hist_original=cv2.calcHist([img],[0],None,[256],[0,256])
hist_equalized=cv2.calcHist([equalized],[0],None,[256],[0,256])
fig, axs= plt.subplots(2,2,figsize=(12,8))
axs[0,0].imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
axs[0,0].set_title('Original IMAGE')
axs[1,0].plot(hist_original, color='black')
axs[1,0].set_title('Histogram(Original)')
axs[1,0].set_xlim([0,256])
axs[0,1].imshow(cv2.cvtColor(equalized,cv2.COLOR_BGR2RGB))
axs[0,1].set_title('Equalized IMAGE')
axs[1,1].plot(hist_original, color='black')
axs[1,1].set_title('Histogram(Equalized)')
axs[1,1].set_xlim([0,256])
plt.tight_layout()
fig.canvas.manager.window.state('zoomed')
plt.show()
