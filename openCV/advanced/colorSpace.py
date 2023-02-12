import cv2 as cv
import numpy as np

img=cv.imread('./images/flower.jpg')
# cv.imshow('cat',img)

scale_percent = 5
width =int(img.shape[1]*scale_percent/100)
height =int(img.shape[0]*scale_percent/100)
dim=(width,height)

# resize
resized = cv.resize(img,dim,interpolation = cv.INTER_AREA)
# original
cv.imshow('Original',resized)

# gray image
gray =cv.cvtColor(resized,cv.COLOR_BGR2GRAY)  # convert    
cv.imshow('gray',gray)


b,g,r = cv.split(resized)
cv.imshow('Blue',b)
cv.imshow('Red',r)
cv.imshow('Green',g)



cv.waitKey(0)