import cv2

img = cv2.imread(r"E:\opencv\learpart3\download.jpg")

if img is None:
    print("null")
else:
    print("The image is", img)

    cv2.imshow("Original", img)

    pt2 = (50, 50)
    pt1= (200, 200)
    color = (0, 0, 255)
    thickness = 4
    cv2.rectangle(img, pt1, pt2, color, thickness)

    cv2.imshow("rectangle drawing", img)
    cv2.imwrite("rectangle.jpg", img)  

    cv2.waitKey(0)
    cv2.destroyAllWindows()