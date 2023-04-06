# import cv2 as cv
# import numpy as  np
# import math

# img = cv.imread("line.jpeg")
# img = cv.resize(img, (500,500))
# cv.imshow("image", img)

# blur = cv.blur(img, (5,5))
# # cv.imshow("blur", blur)

# grey = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
# # cv.imshow("grey", grey)

# canny = cv.Canny(grey, 175, 255)
# cv.imshow("canny", canny)

# lines_detected = img

# lines = cv.HoughLines(canny, 1, np.pi / 180, threshold = 150)
# print(lines)
# if lines is not None:
#     # lines = np.round(lines[0,:]).astype("int")
#     lines = np.round(lines[0,:]).astype("int")

#     print(lines)

# if lines is not None:
#         for i in range(0, len(lines)):
#             rho = lines[i][0]
#             theta = lines[i][0]
#             a = math.cos(theta)
#             b = math.sin(theta)
#             x0 = a * rho
#             y0 = b * rho
#             pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
#             pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
#             cv.line(lines_detected, pt1, pt2, (0,0,255), 1, cv.LINE_AA)


# cv.waitKey(0)



import sys
import math
import cv2 as cv
import numpy as np
def main(argv):
    
    default_file = 'line.jpeg'
    filename = argv[0] if len(argv) > 0 else default_file
    # Loads an image
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_GRAYSCALE)
    src = cv.resize(src, (500,500))
    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        print ('Usage: hough_lines.py [image_name -- default ' + default_file + '] \n')
        return -1
    
    
    dst = cv.Canny(src, 50, 200, None, 3)
    
    # Copy edges to the images that will display the results in BGR
    cdst = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
    cdstP = np.copy(cdst)
    
    lines = cv.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)
    
    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv.line(cdst, pt1, pt2, (0,0,255), 3, cv.LINE_AA)
    
    
    linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)
    
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA)
    
    cv.imshow("Source", src)
    cv.imshow("Detected Lines (in red) - Standard Hough Line Transform", cdst)
    cv.imshow("Detected Lines (in red) - Probabilistic Line Transform", cdstP)
    
    cv.waitKey()
    return 0
    
if __name__ == "__main__":
    main(sys.argv[1:])