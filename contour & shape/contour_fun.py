import cv2
import numpy as np

img = cv2.imread(r"E:\opencv\contour & shape\shape.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh,
    cv2.RETR_TREE,
    cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

for c in contours:
    # ✅ খুব ছোট contour বাদ দাও (noise filter)
    if cv2.contourArea(c) < 500:
        continue

    approx = cv2.approxPolyDP(c, 0.01 * cv2.arcLength(c, True), True)
    corners = len(approx)

    # ✅ moments দিয়ে shape এর exact center বের করো
    M = cv2.moments(c)
    if M["m00"] == 0:
        continue
    X = int(M["m10"] / M["m00"])
    Y = int(M["m01"] / M["m00"])

    if corners == 3:
        label = "Triangle"
    elif corners == 4:
        label = "Rectangle"
    elif corners == 5:
        label = "Pentagon"
    elif corners == 6:
        label = "Hexagon"
    else:
        label = "Circle"

    cv2.putText(img, label, (X, Y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    cv2.drawContours(img, [approx], -1, (0, 255, 0), 3)

cv2.imshow("Original Image", img)
cv2.imwrite("original.jpg", img)
cv2.imshow("Gray Image", gray)
cv2.imwrite("gray.jpg", gray)
cv2.imshow("Thresh Image", thresh)
cv2.imwrite("thresh.jpg", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()