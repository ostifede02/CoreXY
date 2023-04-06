from time import sleep
import cv2 as cv
import CoreXY_functions as coreXY

camera = cv.VideoCapture("video/test_led_video_6.mp4")

while(True):
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

    ret, frame = camera.read()
    cv.imshow("led_detected", coreXY.TrackLed(frame))
    
    sleep(0.1)
    
camera.release()
cv.destroyAllWindows()