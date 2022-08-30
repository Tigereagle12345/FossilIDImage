from __future__ import print_function
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2

def measureRefSize(file):
    # load our input image, convert it to grayscale, and blur it slightly
    image = cv2.imread(file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 0)
    
    # perform edge detection, then perform a dilation + erosion to
    # close gaps in between object edges
    edged = cv2.Canny(gray, 50, 100)
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.erode(edged, None, iterations=1)
    
    # find contours in the edge map
    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    # sort the contours from left-to-right and initialize the bounding box
    # point colors
    (cnts, _) = contours.sort_contours(cnts)
    colors = ((0, 0, 255), (240, 0, 159), (255, 0, 0), (255, 255, 0))
    
    # compute the rotated bounding box of the contour, then
    # draw the contours
    c = cnts[0]
    box = cv2.minAreaRect(c)
    box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
    box = np.array(box, dtype="int")
    cv2.drawContours(image, [box], -1, (0, 255, 0), 2)
    
    # show the original coordinates

    rect = perspective.order_points(box)
    # show the re-ordered coordinates
    #print(rect.astype("int"))
    
    # loop over the original points and draw them
    #for ((x, y), color) in zip(rect, colors):
    #    cv2.circle(image, (int(x), int(y)), 5, color, -1)
    # show the image
    #cv2.imshow("Image", image)
    #cv2.waitKey(0)

    return rect.astype("int")

def imageEdgeSize(file):
    # load our input image, convert it to grayscale, and blur it slightly
    image = cv2.imread(file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 0)
    # perform edge detection, then perform a dilation + erosion to
    # close gaps in between object edges
    edged = cv2.Canny(gray, 50, 100)
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.erode(edged, None, iterations=1)
    # find contours in the edge map
    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    # sort the contours from left-to-right and initialize the bounding box
    # point colors
    (cnts, _) = contours.sort_contours(cnts)
    colors = ((0, 0, 255), (240, 0, 159), (255, 0, 0), (255, 255, 0))
    # loop over the contours individually
    #compute the rotated bounding box of the contour, then
    # draw the contours
    c = cnts[1]
    box = cv2.minAreaRect(c)
    box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
    box = np.array(box, dtype="int")
    cv2.drawContours(image, [box], -1, (0, 255, 0), 2)
    # check to see if the new method should be used for
    # ordering the coordinates
    rect = perspective.order_points(box)
    # show the re-ordered coordinates
    #print(rect.astype("int"))
    return rect.astype("int")

def measureObjectSize(file):
    corners = measureRefSize(file)
    objectCorners = imageEdgeSize(file)
    pixdif = corners[1][0] - corners[0][0]
    ptm = 1 / pixdif
    #print(ptm)
    xsize = objectCorners[1][0] - objectCorners[0][0]
    ysize = objectCorners[2][1] - objectCorners[1][1]
    xsize = xsize * ptm
    ysize = ysize * ptm
    xsize = round(xsize, 2)
    ysize = round(ysize, 2)
    print(xsize)
    print(ysize)

measureObjectSize("fossilpic5.png")
