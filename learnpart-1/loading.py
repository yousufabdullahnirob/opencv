
import cv2

image = cv2.imread("download.jpg")

if image is None:
    print("Image not found")
else:
  print ("Image loaded successfully")