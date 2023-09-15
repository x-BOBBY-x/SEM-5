from math import atan2
import cv2 as cv


def bresenham_circle(img, x0, y0, radius=3):
    x, y, err = (radius, 0, 0)

    points = []
    while x >= y:
        points += [
            (x0 + x, y0 + y),
            (x0 + y, y0 + x),
            (x0 - y, y0 + x),
            (x0 - x, y0 + y),
            (x0 - x, y0 - y),
            (x0 - y, y0 - x),
            (x0 + y, y0 - x),
            (x0 + x, y0 - y),
        ]

        y += 1
        err += 1 + 2 * y
        if 2 * (err - x) + 1 > 0:
            x -= 1
            err += 1 - 2 * x

    h, w = img.shape

    # Sort points in clockwise order
    points = [(x, y, -atan2((y - y0), (x - x0))) for x, y in points if 0 <= x < h and 0 <= y < w]
    points.sort(key=lambda t: t[2])
    points = [(x, y) for x, y, _ in points]

    return points


def FAST(img, threshold=125, n=12):
    features = []

    og = img.copy()
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    for x0, row in enumerate(img):
        for y0, pix in enumerate(row):
            circle = bresenham_circle(img, x0, y0, radius=3)

            # Check fast points
            brighter, darker = 0, 0
            for x, y in circle[::4]:
                if img[x][y] > pix + threshold:
                    brighter += 1
                elif img[x][y] < pix - threshold:
                    darker += 1

            if brighter < 3 and darker < 3:
                continue

            for l in range(len(circle)):
                spice = circle[l:(l + n) % len(circle)]
                if all([img[sx][sy] > pix + threshold for sx, sy in spice]) or all([img[sx][sy] < pix - threshold for sx, sy in spice]):
                    features.append((x0, y0))
                    break

    for x, y in features:
        cv.circle(og, (y, x), 4, (0, 0, 0), -1)

    cv.imshow("Image", og)
    cv.waitKey(0)

    return features


def main():
    img = cv.imread('C:/Users/PG LAB/Desktop/sample.jpg', cv.IMREAD_COLOR)
    FAST(img, threshold=125, n=12)

    return 0


if __name__ == '__main__':
    main()