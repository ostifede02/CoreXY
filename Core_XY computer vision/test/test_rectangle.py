from cv2 import cv2 as cv #Use this form instead of "import cv2" to get rid of cv2 errors in VS Code editor. https://stackoverflow.com/a/61077968/51358
import numpy as np

# Get a reference to webcam #0 (the default one)
video_capture = cv.VideoCapture(0)

def find_square(img):
    thresh = cv.threshold(img, 160, 255, cv.THRESH_BINARY_INV)[1]
    #cv.imshow("Threshhold", thresh)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    close = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel, iterations=2)
    #cv.imshow("Morphology Search", close)
    close = cv.bitwise_not(close)
    #cv.imshow("Invert Search", close)
    cnts = cv.findContours(close, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    min_area = 5000
    max_area = 10000
    image_number = 0
    for c in cnts:
        area = cv.contourArea(c)
        #print(area)
        if area > min_area and area < max_area:
            x, y, w, h = cv.boundingRect(c)
            cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 5)
            print("Width: {}, Height: {}, x: {}, y: {}".format(w,h,x,y))
            image_number += 1
            #print((x, y))
            return True
    return False

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # convert image to grayscale
    img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
  
    # apply a blur using the median filter
    # img = cv2.medianBlur(img, 5)
    img = cv.blur(img, (3, 3))
    
    find_square(img)

    # show image
    cv.imshow('Video', frame)

    # While video window is active, press 'q' on the keyboard to quit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


# Release handle to the webcam
video_capture.release()
cv.destroyAllWindows()