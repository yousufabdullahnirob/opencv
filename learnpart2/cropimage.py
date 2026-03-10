import cv2

img = cv2.imread("E:\opencv\learnpart2\download.jpg")

print(img.shape)

if img is None:
    print("Image not found")
else:
    cv2.imshow("original image", img)
    croped_image = img[100:200, 100:200]           
    cv2.imshow("croped image", croped_image)
    cv2.imwrite("croped image.jpg", croped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()