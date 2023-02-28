import cv2

# Initialize webcam
cap = cv2.VideoCapture(0)

# Set text
text = "MBS3523 Assignment 1 Q4    Name: Cheung Tsz Chun"

# Set font
font = cv2.FONT_HERSHEY_SIMPLEX

# Set color and thickness
color = (255, 0, 0)
thickness = 2

# Get frame width and height
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Load Face Detector Classifier
face_detector = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')

while True:
    # Read frame
    _, frame = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    # Detect faces
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    # Draw rectangle around detected faces
    for (x,y,w,h) in faces:

        # Extract face from frame
        face = frame[y:y+h, x:x+w]

        # Replace face in gray frame
        gray[y:y+h, x:x+w] = face
        cv2.rectangle(gray, (x, y), (x + w, y + h), color, thickness)

    # Draw text
    cv2.putText(gray, text, (int(width / 2 - 200), 20), font, 0.5, color, thickness)

    # Show gray frame
    cv2.imshow("Gray frame", gray)

    # Stop when q is pressed
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

# Release webcam
cap.release()
cv2.destroyAllWindows()
