import cv2
import numpy as numpy
img = cv2.imread(r"E:\opencv\learnpart5\download.jpg")

sharpen_kernal =  numpy.array([[-1,-1,-1],
 [-1,9,-1], 
 [-1,-1,-1]])

sharpened = cv2.filter2D(img, -1, sharpen_kernal)
cv2.imshow('sharpened', sharpened)
cv2.imwrite('sharpened.jpg', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()

