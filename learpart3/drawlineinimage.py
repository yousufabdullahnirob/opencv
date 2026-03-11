import cv2

img = cv2.imread(r"E:\opencv\learpart3\download.jpg")

if img is None:
    print("null")
else:
    print("The image is", img)

    cv2.imshow("Original", img)

    pt1 = (50, 100)
    pt2 = (300, 100)
    color = (0, 0, 255)
    thickness = 4
    cv2.line(img, pt1, pt2, color, thickness)

    cv2.imshow("line drawing", img)
    cv2.imwrite("output.jpg", img)  

    cv2.waitKey(0)
    cv2.destroyAllWindows()

