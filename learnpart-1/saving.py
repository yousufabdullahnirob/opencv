
import cv2

image = cv2.imread(r"E:\opencv\learnpart-1\download.jpg")

if image is not None:
  success = cv2.imwrite("saved_image.jpg", image) # save the image
  if success:
    print("Image saved successfully")
  else:
    print("Image not saved")
else:
    print("Image not found")