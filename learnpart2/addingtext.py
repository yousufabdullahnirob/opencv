import cv2
import numpy as np

img = cv2.imread(r"E:\opencv\learpart3\download.jpg")

if img is None:
    print("null")
else:
    print("The image is", img)

    cv2.imshow("Original", img)

    cv2.putText(img, "Hello World", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Text Drawing", img)
    cv2.imwrite("text.jpg", img)  

    cv2.waitKey(0)
    cv2.destroyAllWindows()