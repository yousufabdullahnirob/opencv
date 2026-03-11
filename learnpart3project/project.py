import cv2
import numpy as np

path = input("Image path: ").strip("\"'")
img = cv2.imread(path)

if img is None:
    print("Image load hoyni! Verify the path is correct and exists.")
else:
    img_copy = img.copy()
    current_shape = "rectangle"
    typed_text = ""

    def draw_shape(event, x, y, flags, param):
        global img, current_shape, typed_text  # ← এটাই fix

        if event == cv2.EVENT_LBUTTONDOWN:
            print(f"Mouse clicked at ({x}, {y}) - Drawing {current_shape}")
            if current_shape == "rectangle":
                cv2.rectangle(img, (x-50, y-50), (x+50, y+50), (0,255,0), 2)

            elif current_shape == "circle":
                cv2.circle(img, (x,y), 50, (255,0,0), 2)

            elif current_shape == "triangle":
                pts = np.array([[x, y-50],[x-50, y+50],[x+50, y+50]], np.int32)
                cv2.polylines(img, [pts.reshape((-1,1,2))], True, (0,0,255), 2)

            elif current_shape == "text" and typed_text != "":
                cv2.putText(img, typed_text, (x,y),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2)

            cv2.imshow("Image", img)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", draw_shape)

    print("\n" + "="*50)
    print(" IMPORTANT: Click on the Image Window to focus it!")
    print(" Keys typed in this terminal will NOT work.")
    print("="*50)
    print("\n[R] Rectangle  [C] Circle  [T] Triangle")
    print("[W] Type text  [Z] Reset  [Q] Quit\n")

    while True:
        try:
            # Check if the user closed the window by clicking the 'X'
            if cv2.getWindowProperty("Image", cv2.WND_PROP_VISIBLE) < 1:
                break
        except:
            break

        key = cv2.waitKey(1) & 0xFF

        if key != 255: # If a key was pressed
            try:
                char_pressed = chr(key).lower()
            except ValueError:
                continue

            if char_pressed == 'r':
                current_shape = "rectangle"
                print("→ Selected: Rectangle (Now click on the image)")

            elif char_pressed == 'c':
                current_shape = "circle"
                print("→ Selected: Circle (Now click on the image)")

            elif char_pressed == 't':
                current_shape = "triangle"
                print("→ Selected: Triangle (Now click on the image)")

            elif char_pressed == 'w':
                current_shape = "text"
                print("→ Text mode! Please switch to THIS terminal to type.")
                typed_text = input("Type your text here: ")
                print(f"→ Text recorded: '{typed_text}'. Now click on the IMAGE WINDOW to place it.")

            elif char_pressed == 'z':
                img = img_copy.copy()
                cv2.imshow("Image", img)
                cv2.setMouseCallback("Image", draw_shape)
                print("→ Image Reset!")

            elif char_pressed == 'q':
                break

    cv2.destroyAllWindows()
     