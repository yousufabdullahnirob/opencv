import cv2

img = cv2.imread(r"E:\opencv\learpart3\download.jpg")

if img is None:
    print("null")
else:
    print("The image is", img)

    cv2.imshow("Original", img)

    center = (100, 100)
    radius = 50
    color = (0, 0, 255)
    thickness = -1
    cv2.circle(img, center, radius, color, thickness)

    cv2.imshow("circle drawing", img)
    cv2.imwrite("circle.jpg", img)  

    cv2.waitKey(0)
    cv2.destroyAllWindows()