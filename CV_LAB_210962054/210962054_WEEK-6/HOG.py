import cv2

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

image = cv2.imread('C:/Users/PG LAB/Desktop/R.jpg')

img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
rects, weights = hog.detectMultiScale(img_gray, winStride=(2, 2), padding=(10, 10), scale=1.02)
for i, (x, y, w, h) in enumerate(rects):
    if weights[i] < 0.13:
        continue
    elif weights[i] < 0.3 and weights[i] > 0.13:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    if weights[i] < 0.7 and weights[i] > 0.3:
        cv2.rectangle(image, (x, y), (x + w, y + h), (50, 122, 255), 2)
    if weights[i] > 0.7:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.putText(image, 'High confidence', (10, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.putText(image, 'Moderate confidence', (10, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (50, 122, 255), 2)
cv2.putText(image, 'Low confidence', (10, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
cv2.imshow('HOG detection', image)
cv2.waitKey(0)
