import cv2 as cv
import numpy as np
img=cv.imread('./images/cat1.png')

# rotate
rotated = cv.rotate(img,cv.ROTATE_90_CLOCKWISE)
cv.imshow('rotated',rotated)
cv.waitKey(0)

# flip
# 0->vertical
# 1->horizontal
# -1->both
flipped = cv.flip(img,-1)
cv.imshow('flipped',flipped)
cv.waitKey(0)

# translate
Mat = np.float32([[1,0,25],[0,1,50]])
shifted = cv.warpAffine(img,Mat,(img.shape[1],img.shape[0]))
cv.imshow('Shifted down and right',shifted)
cv.waitKey(0)
