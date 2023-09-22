import cv2
import numpy as np

# Load the query image
query_image = cv2.imread('C:/Users/PG LAB/Desktop/test.jpg')

# Compute the color histogram of the query image
query_hist = cv2.calcHist([query_image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
print(query_hist)
# Load the database images
database_images = []
for i in range(8):
    database_image = cv2.imread(f"test{i}.jpg")
    database_images.append(database_image)

# Compute the color histograms of the database images
database_hists = []
for database_image in database_images:
    database_hist = cv2.calcHist([database_image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    database_hists.append(database_hist)

# Compute the similarity between the query image histogram and the database image histograms
similarities = []
for database_hist in database_hists:
    similarity = cv2.compareHist(query_hist, database_hist, cv2.HISTCMP_CORREL)
    similarities.append(similarity)

# Sort the database images by similarity
sorted_database_images = sorted(zip(database_images, similarities), key=lambda x: x[1], reverse=True)

# Display the most similar images
for i in range(8):
    database_image, similarity = sorted_database_images[i]
    cv2.imshow(f"Image {i + 1}", database_image)
    cv2.waitKey(0)

cv2.destroyAllWindows()