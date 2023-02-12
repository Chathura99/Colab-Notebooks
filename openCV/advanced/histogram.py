import matplotlib.pyplot as plt
import cv2 as cv


# load
img=cv.imread('./images/cat1.png')
cv.imshow('ori',img)

cv.waitKey(0)
# gray image

gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)  # convert   

# histogram
histro = cv.calcHist([gray],[0],None,[256],[0,256])

plt.figure()
plt.title('Histogram - cat image')
plt.xlabel('Bins')
plt.ylabel('No of pixels')
plt.plot(histro)
plt.show()

