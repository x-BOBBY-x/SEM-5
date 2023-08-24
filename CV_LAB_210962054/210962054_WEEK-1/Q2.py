import cv2

image = cv2.imread('C:/Users/PG LAB/Desktop/sample.jpg',cv2.IMREAD_UNCHANGED)

window_name = 'making a rectangle'
start_point = (5,5)
end_point = (100,100)
color = (255,50,0)
thickness = 2
image = cv2.rectangle(image,start_point, end_point, color, thickness)
cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()