
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
src = cv.imread('C:/Users/PG LAB/Desktop/sample.jpg')
kernel1 = np.ones((3, 3), np.float32)/9
dst=cv.filter2D(src,-1,kernel1)
fig, axs= plt.subplots(1,2)
axs[0].imshow(cv.cvtColor(src,cv.COLOR_BGR2RGB))
axs[0].set_title('Original IMAGE')
axs[1].imshow(cv.cvtColor(dst,cv.COLOR_BGR2RGB))
axs[1].set_title('blurred IMAGE')
plt.show()
