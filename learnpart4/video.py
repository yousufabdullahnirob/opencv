import cv2

cap = cv2.VideoCapture(0)  

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'mp4v')  

recorder = cv2.VideoWriter('output.mp4', codec, 20, (frame_width, frame_height))  # ✅ .avi → .mp4

while True:
    ret, frame = cap.read()
    if not ret:
        break
    recorder.write(frame)
    cv2.imshow('Record Live', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
recorder.release()
cv2.destroyAllWindows()