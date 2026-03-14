import cv2

img = cv2.imread(r"E:\opencv\learnpart6\flower.png",
 cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(img, 50, 150)

cv2.imshow("Original Image", img)
cv2.imwrite("original.jpg", img)
cv2.imshow("Edges", edges)
cv2.imwrite("edges.jpg", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()