import cv2
import numpy as np

img = cv2.imread(r"E:\opencv\learpart3\download.jpg")

if img is None:
    print("null")
else:
    print("The image is", img)

    cv2.imshow("Original", img)

   
    pts = np.array([[150, 50], [50, 200], [250, 200]], np.int32)
    pts = pts.reshape((-1, 1, 2))  

    color = (0, 0, 255)
    thickness = -1  

    cv2.fillPoly(img, [pts], color)

    cv2.imshow("Triangle Drawing", img)
    cv2.imwrite("triangle.jpg", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()