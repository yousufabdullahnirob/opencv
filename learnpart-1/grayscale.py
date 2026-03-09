import cv2

image = cv2.imread(r"E:\opencv\learnpart-1\download.jpg")

if image is not None:
    print("Image loaded successfully")
    cv2.imshow("Image", image) # open a window to display the image
    cv2.waitKey(0)            # wait for a key press
    cv2.destroyAllWindows() # close the window
    height, width, channels = image.shape
    print("Height: ", height)
    print("Width: ", width)
    print("Channels: ", channels)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")