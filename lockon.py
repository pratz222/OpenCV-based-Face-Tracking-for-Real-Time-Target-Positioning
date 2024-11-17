import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(0)


tracker = cv2.TrackerCSRT_create()
tracking = False 

while True:
    
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

   
    if tracking:
       
        success, box = tracker.update(frame)
        if success:
            
            x, y, w, h = map(int, box)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Display center coordinates for the tracked face
            center_x, center_y = x + w // 2, y + h // 2
            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)
            cv2.putText(frame, f"Target Position: ({center_x}, {center_y})", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        else:
            # Reset tracking if we lose the face
            tracking = False
            cv2.putText(frame, "Lost target. Re-detecting...", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Detect faces when not tracking
    if not tracking:
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
           
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
            tracker.init(frame, (x, y, w, h))
            tracking = True
            break 

    
    cv2.imshow("Face Tracking for Target Positioning", frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
