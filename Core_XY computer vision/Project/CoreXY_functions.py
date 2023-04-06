import cv2 as cv

def TrackLed(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (7,7), 0)

    (minVal, maxVal, minLoc, maxLoc) = cv.minMaxLoc(blur)
    
    coordinates = list(maxLoc)
    coordinates[0] = coordinates[0]+15
    
    cv.circle(frame, maxLoc, 5, (0, 0, 255), 2)
    cv.putText(frame, str(maxLoc), (coordinates), 5, 0.8, (0,0,255), 1)

    return frame