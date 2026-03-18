import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)#1.1 is scale factor and 4 is minNeighbors
    #detectMultiScale() returns a list of rectangles where faces are detected
    for x, y, w, h in faces:#for each face detected
        #using for loop to draw rectangle around the face
        #x and y are the top left corner of the rectangle and w and h are the width and height of the rectangle
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)#(255, 0, 0) is color and 2 is thickness
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()