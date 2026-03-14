import cv2
img = cv2.imread(r"E:\opencv\learnpart5\download.jpg")

blur = cv2.medianBlur(img, 5)

cv2.imshow('image', img)
cv2.imshow('median_blur', blur)
cv2.imwrite("median_blur.jpg", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()