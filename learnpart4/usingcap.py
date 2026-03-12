import cv2 

cap = None

for i in range(3):
    cap = cv2.VideoCapture(i, cv2.CAP_MSMF)
    if cap is None or not cap.isOpened():
        print(f"Warning: unable to open video source {i} with MSMF")
    else:
        print(f"Success! Opened camera {i} with MSMF")
        break

if cap is None or not cap.isOpened():
    print("Cannot open any camera index. Please ensure the camera is connected and not used by another app.")
    exit()


while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    cv2.imshow("Frame", frame)
    cv2.imwrite("frame.jpg", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
