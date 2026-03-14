import cv2
img = cv2.imread(r"E:\opencv\learnpart5\images.jpg")
cv2.imwrite(r"E:\opencv\learnpart5\images.jpg", img)

blur = cv2.GaussianBlur(img, (5, 5), 0)

cv2.imshow('image', img)
cv2.imshow('blur', blur)
cv2.imwrite("blur.jpg", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()