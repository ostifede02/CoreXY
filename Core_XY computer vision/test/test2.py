#Detect circles with a webcam using opencv
from cv2 import cv2 #Use this form instead of "import cv2" to get rid of cv2 errors in VS Code editor. https://stackoverflow.com/a/61077968/51358
import numpy as np

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    cv2.rectangle(frame, (10,10), (630,470),(0,0,255), 2)
    print(frame.shape)

    # convert image to grayscale
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  
    # apply a blur using the median filter
    # img = cv2.medianBlur(img, 5)
    img = cv2.blur(img, (3, 3))
    
    # find circles in grayscale image using the Hough transform
    circles = cv2.HoughCircles(image=img, method=cv2.HOUGH_GRADIENT, dp=0.9, 
                            minDist=50, param1=110, param2=39, minRadius=0, maxRadius=30)

    if np.any(circles):
        print("------------------")
        print("number of circles: ", len(circles[0, :]))
        for co, i in enumerate(circles[0, :], start=1):
            # draw the outer circle with radius i[2] in green
            cv2.circle(frame,(int(i[0]),int(i[1])),int(i[2]),(0,255,0),2)
            # draw the center as a circle with radius 2 in red
            cv2.circle(frame,(int(i[0]),int(i[1])),2,(0,0,255),3)
            print("center of circle: ", i[0], ", ",i[1])
    else:
        print("No circles detected.")
    # show image
    cv2.imshow('Video', frame)

    # While video window is active, press 'q' on the keyboard to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()