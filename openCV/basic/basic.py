import cv2 as cv
# read image
# img=cv.imread('./images/cat1.png')
# cv.imshow('cat',img)
# cv.waitKey(0)

# read video
video=cv.VideoCapture('./videos/Squirrel.mp4')

if(video.isOpened()==False) :
    print('Error')

while(video.isOpened()) :
    # capture frame by frame
    ret,frame =video.read()
    if ret ==True:
        # display result frame
        cv.imshow('Frame',frame)
        # press Q to exit
        if cv.waitKey(5) & 0xFF==ord('q'):
            break
    else:
        break
