import cv2 as cv
import numpy as np


# load
img = cv.imread('./images/cat1.png')
cv.imshow('ori', img)

# gray image

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # convert

# several algo for edge detection

# 1. laplacian
lap = cv.Laplacian(gray, cv.CV_64FC1)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian', lap)


# 1. sobel
soblex = cv.Sobel(gray, cv.CV_64F, 0, 1)
sobley = cv.Sobel(gray, cv.CV_64F, 1, 0)
cv.imshow('soblex', soblex)
cv.imshow('sobley', sobley)


cv.waitKey(0)
