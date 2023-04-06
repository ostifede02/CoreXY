import cv2 as cv

camera = cv.VideoCapture(0)

while(True):
    ret, frame = camera.read()
    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv.destroyAllWindows()