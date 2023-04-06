import cv2 as cv
import numpy as  np

img = cv.imread("test_marker_5.jpeg")
print(img.shape)
cv.imshow("image", img)

blur = cv.blur(img, (5,5))
# cv.imshow("blur", blur)

grey = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
# cv.imshow("grey", grey)

circles_detected = img

circles = cv.HoughCircles(grey,  method=cv.HOUGH_GRADIENT, dp=1, param1=200, minDist=1)

if circles is not None:
    # circles = np.round(circles[0,:]).astype("int")
    circles = np.round(circles[0,:]).astype("int")

    print(circles)

    for (x, y, r) in circles:
        cv.circle(circles_detected, (x, y), r, (0, 255, 0), 1)
        cv.circle(circles_detected, (x, y), 1, (0, 0, 255), 1)

circles_detected = cv.resize(circles_detected, (450,600))
cv.imshow("circles_detected", circles_detected)

cv.waitKey(0)