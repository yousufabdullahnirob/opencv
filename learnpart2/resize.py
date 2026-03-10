import cv2

img = cv2.imread("E:\opencv\learnpart2\download.jpg")

print(img.shape)

if img is None:
    print("Image not found")
else:
    cv2.imshow("original image", img)
    resized = cv2.resize(img, (500, 500))
    cv2.imshow("resized image", resized)
    cv2.imwrite("resized image.jpg", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()