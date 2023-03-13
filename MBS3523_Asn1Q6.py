import cv2
EVT = 0

def drawShape(event,x,y,flags,params):
    global EVT
    global PNT1
    global PNT2
    if event == cv2.EVENT_LBUTTONDOWN:
        PNT1 = (x,y)
        EVT = event
    elif event == cv2.EVENT_LBUTTONUP:
        PNT2 = (x,y)
        EVT = event

    elif event == cv2.EVENT_RBUTTONUP:
        EVT = event
cv2.namedWindow('image')
cv2.setMouseCallback('image',drawShape)


cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    ret,image = cam.read()
    cv2.putText(image, 'MBS3523 Assignment 1 Q6    Name: Cheung Tsz Chun',
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    if EVT == 4:
        cv2.rectangle(image,PNT1,PNT2,(255,0,0),2)
        ROI = image[PNT1[1]:PNT2[1],PNT1[0]:PNT2[0]] # python format [0],[1] (x,y,z...) ; row and column
        cv2.imshow('ROI',ROI)
    if EVT == 5:
        image[:,:] = image
        try:
            cv2.destroyWindow('ROI')
        except:
            ENT=0
    cv2.imshow('image',image)

    if cv2.waitKey(1) & 0xff == 27:
        break
cam.release()
cv2.destroyAllWindows()
