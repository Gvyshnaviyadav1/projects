import cv2
import numpy as np

# Haarcascade file path (make sure this file is uploaded)
haar_file = 'haarcascade_frontalface_alt.xml' # Load Haarcascade for face detection
face_cascade = cv2.CascadeClassifier(haar_file)
cap = cv2.VideoCapture(0)
    
while True:
    # Read frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Error: Couldn't read frame.")
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   

  

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), ( 0,255, 0), 2)

    # Show the image with detected faces
    cv2.imshow('Detected Faces', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()    
cv2.destroyAllWindows()
