import cv2 as cv
import numpy as np

img=cv.imread('./images/cat1.png')
cv.imshow('ori',img)

blurImg = cv.blur(img,(10,10))
cv.imshow('blur',blurImg)

# blurMoreImg = cv.blur(img,(100,100))
# cv.imshow('blur',blurMoreImg)

cv.waitKey(0)
