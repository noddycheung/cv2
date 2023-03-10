import cv2
print(cv2.__version__)

cam= cv2.VideoCapture(0)
while True:
    success,frame=cam.read()
    grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)

    cv2.imshow('Black white image', blackAndWhiteImage)
    cv2.imshow('Original image', frame)

    if cv2.waitKey(2)&0xff==27:
        break
cam.release()
cv2.destroyAllWindows()
