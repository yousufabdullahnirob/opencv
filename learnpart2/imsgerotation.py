import cv2

img = cv2.imread("E:\opencv\learnpart2\download.jpg")

print(img.shape)

if img is None:
    print("Image not found")
else:
   cv2.imshow("original image", img)
img_rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)     
img_center = (img.shape[0] // 2, img.shape[1] // 2)   
cv2.imshow("center", img_center)
cv2.imwrite("center.jpg", img_center) 
cv2.imshow("rotated image", img_rotated)
cv2.imwrite("rotated image.jpg", img_rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
m = cv2.getRotationMatrix2D(img_center, 45, 1) 
img_rotated = cv2.warpAffine(img, m, (img.shape[1], img.shape[0]))
cv2.imshow("rotated image", img_rotated)
cv2.imwrite("rotated image.jpg", img_rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

    #fliping image
img_flipped = cv2.flip(img, 1)
img_flipped_x = cv2.flip(img, 0)
img_flipped_xy = cv2.flip(img, -1)
cv2.imshow("flipped image", img_flipped)
cv2.imshow("flipped image x", img_flipped_x)
cv2.imshow("flipped image xy", img_flipped_xy)
cv2.imwrite("flipped image.jpg", img_flipped)
cv2.imwrite("flipped image x.jpg", img_flipped_x)
cv2.imwrite("flipped image xy.jpg", img_flipped_xy)
cv2.waitKey(0)
cv2.destroyAllWindows()