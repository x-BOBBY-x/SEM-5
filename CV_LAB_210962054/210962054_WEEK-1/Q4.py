import cv2

# path
path =r'C:/Users/PG LAB/Desktop/sample.jpg'

# Reading an image in default mode
src = cv2.imread(path)

# Window name in which image is displayed
window_name = 'Rotated Image'

# Using cv2.rotate() method
# Using cv2.ROTATE_90_CLOCKWISE rotate
# by 90 degrees clockwise
image = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)
image1 = cv2.rotate(src, cv2.ROTATE_180)
image2 = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)
# image3 = cv2.rotate(src, cv2.RotateFlags)

# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.imshow(window_name, image1)
cv2.waitKey(0)
cv2.imshow(window_name, image2)
cv2.waitKey(0)
# cv2.imshow(window_name, image3)
# cv2.waitKey(0)