import cv2 as cv
import numpy as np

# blank image with scalr and number of color channels and type as image
blank = np.zeros((500, 500, 3), dtype='uint8')

# painting
blank[:] = 0, 255, 0  # whole

cv.putText(blank,
           text='Chathura',
           org=(100, 200),
           fontFace=cv.FONT_HERSHEY_SIMPLEX,
           fontScale=1,
           color=(0, 0, 255),
           thickness=2
           )


# show
cv.imshow('blank-green', blank)
cv.waitKey(0)
