import cv2
print(cv2.__version__)
dispW = 640
dispH = 480
flip = 2
cam= cv2.VideoCapture(0)
dispW=int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
dispH=int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
BW=80
BH=80
posX=10
posY=270
dx=2
dy=2

text = "MBS3523 Assignment 1 Q3    Name: Cheung Tsz Chun"
width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))

font = cv2.FONT_HERSHEY_SIMPLEX


while True:
    ret, frame = cam.read()
    cv2.putText(frame, text, (int(width / 2 - 200), 20), font, 0.5, (255,0,0), 2)
    frame=cv2.rectangle(frame,(posX,posY),(posX+BW,posY+BH),(0,0,255),2)
    posX=posX+dx
    posY=posY+dy
    if posX<=0 or posX+BW>=dispW:
        dx=dx*(-1)
    if posY<=0 or posY+BH>=dispH:
        dy=dy*(-1)
    cv2.imshow('nanoCam', frame)
    if cv2.waitKey(1)==27:
        break
cam.release()
cv2.destroyAllWindows()
