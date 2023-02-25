import cv2
print (cv2.__version__)

dispW = 640
dispH = 480

text = "MBS3523 Assignment 1 Q5    Name: Cheung Tsz Chun"

# Set font
font = cv2.FONT_HERSHEY_SIMPLEX


cam= cv2.VideoCapture(0)

def nil(x):
    pass

cv2.namedWindow('frame')
cv2.createTrackbar('x','frame',100,dispW,nil)
cv2.createTrackbar('y','frame',100,dispH,nil)

while True:
    success, frame = cam.read()
    x=cv2.getTrackbarPos('x','frame')
    y=cv2.getTrackbarPos('y','frame')
    cv2.line(frame,(x,0),(x,dispH),(255,0,0),2)
    cv2.line(frame, (0, y), (dispW, y), (255, 0, 0), 2)
    cv2.putText(frame, text, (int(dispW / 2 - 200), 20), font, 0.5, (0,255,0), 2)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xff == 27:
        break
cam.release()
cv2.destroyAllWindows()
