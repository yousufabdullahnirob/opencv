import cv2

image_path = input("Enter image path: ")
output_name = input("Enter name for grayscale image (e.g. gray.jpg): ")

image = cv2.imread(image_path)

if image is not None:
    print("Image loaded successfully")

    height, width, channels = image.shape
    print("Height:", height)
    print("Width:", width)
    print("Channels:", channels)

   
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    
    cv2.imwrite(output_name, gray_image)
    print(f"Grayscale image saved as: {output_name}")

    cv2.imshow("Original", image)
    cv2.imshow("Grayscale", gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found. Check the path!")


