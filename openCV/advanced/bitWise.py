import cv2 as cv
import numpy as np

# img=cv.imread('./images/cat1.png')
# cv.imshow('ori',img)

blank = np.zeros((500, 500, 3), dtype='uint8')

# rectangle
rec=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
cv.imshow('rec',rec)
cv.waitKey(0)

# circle
cir=cv.circle(blank.copy(),(200,200),200,255,-1) #position,radius,color,fill
cv.imshow('cir',cir)
cv.waitKey(0)

# bitwise
Bitwise_and=cv.bitwise_and(rec,cir)
cv.imshow('and',Bitwise_and)
cv.waitKey(0)

Bitwise_or=cv.bitwise_or(rec,cir)
cv.imshow('or',Bitwise_or)
cv.waitKey(0)

img=cv.imread('./images/cat1.png')
# create mask
mask=np.zeros(img.shape[:2],dtype='unit8')

cirMask=cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow('cirMask',cirMask)
cv.waitKey(0)

# cropped
maskedImg =cv. bitwise_and(img,img,mask=cirMask)
cv.imshow('masked',maskedImg)


