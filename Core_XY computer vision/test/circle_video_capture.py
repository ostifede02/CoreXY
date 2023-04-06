import cv2 as cv
import numpy as np

lower_color = np.array([170, 50, 50])
upper_color = np.array([180, 255, 255])

def Elab_Image(image):
    blur = cv.blur(image, (5,5))
    hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, lower_color, upper_color)
    mask_color = cv.bitwise_and(blur, blur, mask = mask)
    color_to_gray = cv.cvtColor(mask_color, cv.COLOR_BGR2GRAY)
    canny_edge = cv.Canny(color_to_gray, 50, 240)

    return canny_edge


camera = cv.VideoCapture("video/test_marker_video_3.mp4")

while(True):
    ret, frame = camera.read()
        
    img_elaborate = Elab_Image(frame)
    cv.imshow("img_elaborate", img_elaborate)
    circles_detected = frame
    circles = cv.HoughCircles(img_elaborate, method=cv.HOUGH_GRADIENT, dp=1,param1=200, minRadius=0, maxRadius=50, minDist=1)

    if circles is not None:
        # circles = np.round(circles[0,:]).astype("int")
        circles = np.round(circles[0,:]).astype("int")

        print(circles)

        for (x, y, r) in circles:
            cv.circle(circles_detected, (x, y), r, (0, 255, 0), 1)
            cv.circle(circles_detected, (x, y), 1, (0, 0, 255), 1)


    cv.circle(circles_detected, (100, 30), 4, (0, 0, 255), 1)
    cv.imshow("circles_detected", circles_detected)
    cv.waitKey(0)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
camera.release()
cv.destroyAllWindows()