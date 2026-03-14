import cv2

img = cv2.imread(r"learnpart6/man.png",
 cv2.IMREAD_GRAYSCALE)
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)



cv2.imshow("Original Image", img)
cv2.imwrite("original.jpg", img)
cv2.imshow("thresh", thresh)
cv2.imwrite("thresh.jpg", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()