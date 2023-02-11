import cv2 as cv
# img=cv.imread('./images/cat2.jpg')
img=cv.imread('./images/cat1.png')

scale_percent = 40
width =int(img.shape[1]*scale_percent/100)
height =int(img.shape[0]*scale_percent/100)
dim=(width,height)
# dim=(600,200)

# resize
resized = cv.resize(img,dim,interpolation = cv.INTER_AREA)
print('resized dim : ',resized.shape)
cv.imshow('resized image',resized)
cv.waitKey(0)