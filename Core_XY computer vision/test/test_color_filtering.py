import cv2 as cv
import numpy as np

def Elab_Image(image):
    blur = cv.blur(image, (5,5))
    hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, lower_green, upper_green)
    mask_colorr = cv.bitwise_and(blur, blur, mask = mask)
    color_to_gray = cv.cvtColor(mask_colorr, cv.COLOR_BGR2GRAY)
    canny_edge = cv.Canny(color_to_gray, 50, 240)

    return canny_edge

lower_green = np.array([50, 100, 255])
upper_green = np.array([10, 10, 255])


image = cv.imread("images/test_marker_7.jpeg")
image = cv.resize(image, (600,800))
cv.imshow("image", image)

blur = cv.blur(image, (5,5))

hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv, lower_green, upper_green)
mask_color = cv.bitwise_and(blur, blur, mask = mask)
color_to_gray = cv.cvtColor(mask_color, cv.COLOR_BGR2GRAY)
canny_edge = cv.Canny(color_to_gray, 50, 240)

cv.imshow("color_to_gray", color_to_gray)
cv.imshow("mask_color", mask_color)
cv.imshow("mask", mask)
cv.imshow("canny_edge", canny_edge)



circles_detected = image

circles = cv.HoughCircles(canny_edge,  method=cv.HOUGH_GRADIENT, dp=1,  minDist=50, param1=120, param2=40, minRadius=20, maxRadius=80)

if circles is not None:
    circles = np.round(circles[0,:]).astype("int")

    print(circles)

    for (x, y, r) in circles:
        cv.circle(circles_detected, (x, y), r, (0, 255, 0), 1)
        cv.circle(circles_detected, (x, y), 1, (0, 0, 255), 1)
else:
    print("NO circles has found!")

cv.imshow("circles_detected", circles_detected)

cv.waitKey(0)


# **********************************************************************************************


# cnts = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
# # Extract contours depending on OpenCV version
# cnts = cnts[0] if len(cnts) == 2 else cnts[1]

# # Iterate through contours and filter by the number of vertices 
# for c in cnts:
#     perimeter = cv.arcLength(c, True)
#     approx = cv.approxPolyDP(c, 0.04 * perimeter, True)
#     if len(approx) > 5:
#         cv.drawContours(image, [c], -1, (36, 255, 12), -1)

# cv.imshow("image_circle", image)