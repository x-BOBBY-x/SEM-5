import cv2 as cv
import numpy as np


def my_harris(img):
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    dx = cv.Sobel(img_gray, cv.CV_64F, dx=1, dy=0)
    dy = cv.Sobel(img_gray, cv.CV_64F, dx=0, dy=1)

    dx2 = np.square(dx)
    dy2 = np.square(dy)
    dxdy = dx * dy

    b_dx2 = cv.boxFilter(dx2, -1, (3, 3))
    b_dy2 = cv.boxFilter(dy2, -1, (3, 3))
    b_dxdy = cv.boxFilter(dxdy, -1, (3, 3))

    harris = b_dx2 * b_dy2 - np.square(b_dxdy) - 0.12 * np.square(b_dx2 + b_dy2)

    cv.normalize(harris, harris, 0, 1, cv.NORM_MINMAX)

    threshold = 0.65
    loc = np.where(harris >= threshold)

    for pt in zip(*loc[::-1]):
        cv.circle(img, pt, 3, (0, 0, 255), -1)


def inbuilt_harris(img):
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    inbuilt = cv.cornerHarris(img_gray, 2, 3, 0.04)

    thresh = 0.1 * inbuilt.max()
    for j in range(0, inbuilt.shape[0]):
        for i in range(0, inbuilt.shape[1]):
            if inbuilt[j, i] > thresh:
                # image, center pt, radius, color, thickness
                cv.circle(img, (i, j), 3, (255, 0, 0), -1)


def main():
    img = cv.imread('C:/Users/PG LAB/Desktop/sample.jpg')
    img_copy = np.copy(img)

    my_harris(img)
    inbuilt_harris(img_copy)

    cv.imshow('Custom', img)
    cv.imshow('Inbuilt', img_copy)
    cv.waitKey(0)

    cv.destroyAllWindows()


if __name__ == '__main__':
    main()