import numpy as np
import cv2

def TrackLed(frame):
    frame = cv2.resize(frame, (600,800))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)

    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(blur)
    cv2.circle(frame, maxLoc, 4, (0, 0, 255), 1)

    return frame


image = cv2.imread("images/test_led_1.jpeg")
image = TrackLed(image)

cv2.imshow("Result", image)
cv2.waitKey(0)