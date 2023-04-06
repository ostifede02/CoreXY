# USAGE
# python detect_bright_spots.py --image images/lights_01.png
# Import necessary packages 
from imutils import contours
from skimage import measure
import numpy as np
import argparse
import imutils
import cv2
dict = {
}
def imageShow(name, image, end=False):
cv2.imshow(name, image)
cv2.waitKey(0)
# dict[name] = image
# if end:
# for i, j in enumerate(dict.items()):
# name = str("image/" + str(i + 1) + j[0] + ".jpg")
# print(name)
# cv2.imshow(name, j[1])
# cv2.waitKey(0)
# cv2.imwrite(str("image/" + str(i + 1) + ".jpg"), j[1])
# Build command line parameters and parse 
# --image Original image path 
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
help="path to the image file")
args = vars(ap.parse_args())
# Load image from disk , Convert it to grayscale , smooth （ It's fuzzy ） To reduce high frequency noise ：
image = cv2.imread(args["image"])
origin = image.copy()
imageShow("origin", origin)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
imageShow("gray", gray)
imageShow("blurred", blurred)
imageShow("gray VS blurred", np.hstack([gray, blurred]))
# To display the brightest area in the blurred image , Threshold needs to be applied 
# The thresholding method is applied to the smoothed image , To show a bright area 
# For any pixel value p> = 200 And set it to 255（ white ）. <200 The pixel value of is set to 0（ black ）.
thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)[1]
imageShow("thresh1", thresh)
# There is still some noise in the image （ Small spots ）, It can be cleaned by performing a series of corrosion and expansion ：
# Apply a series of corrosion tests 、 Expand to eliminate small noise 
thresh = cv2.erode(thresh, None, iterations=2)
thresh = cv2.dilate(thresh, None, iterations=4)
imageShow("thresh2", thresh)
# After application of corrosion expansion operation , The threshold image is much cleaner , But there are still some spots to remove 
# The key step of the project is to mark each area in the above figure . however , Even after application of erosion and expansion , Still want to filter out all the remaining “ noisy ” Area . A good way to do this is to perform link component analysis ：
# Apply connection component analysis to thresholded images , initialization mask To store the largest element 
# Use scikit-image The library performs the actual link component analysis 
labels = measure.label(thresh, neighbors=8, background=0)
mask = np.zeros(thresh.shape, dtype="uint8")
# Traverse unique components 
for (i, label) in enumerate(np.unique(labels)):
# If black mark , Filter 
if label == 0:
continue
# otherwise , Build a component mask And count the number of pixels 
labelMask = np.zeros(thresh.shape, dtype="uint8")
labelMask[labels == label] = 255
numPixels = cv2.countNonZero(labelMask)
# If the component is large enough , exceed 300 Pixels are added to the large speckle mask 
if numPixels > 300:
mask = cv2.add(mask, labelMask)
imageShow("mask" + str(i), mask)
# Please note that , How to filter out all small spots , And keep only large spots .
# Find the outline in the mask image , And sort from left to right 
cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = contours.sort_contours(cnts)[0]
# Traverse all the contours 
for (i, c) in enumerate(cnts):
# Draw bright spots in the image 
# Calculate the minimum bounding circle of the contour , Represents the bright area in the image 
(x, y, w, h) = cv2.boundingRect(c)
((cX, cY), radius) = cv2.minEnclosingCircle(c)
cv2.circle(image, (int(cX), int(cY)), int(radius),
(0, 0, 255), 3)
cv2.putText(image, "#{}".format(i + 1), (x, y - 15),
cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
# Show output image 
imageShow("ResImage", image, True)
imageShow("origin VS ResImage", np.hstack([origin, image]))
cv2.destroyAllWindows()