import cv2
import serial,time
import numpy as np

classesFile = 'For YOLO/For YOLO/coco80.names'
classes = open(classesFile, 'r').read().splitlines()
confThreshold = 0.6

net = cv2.dnn.readNetFromDarknet('For YOLO/For YOLO/yolov3-320.cfg', 'For YOLO/For YOLO/yolov3-320.weights')
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

class_of_interest = 67  # index of "remote"

cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)
#fourcc= cv2.VideoWriter_fourcc(*'XVID')
ArduinoSerial=serial.Serial('com6',9600,timeout=0.1)
#out= cv2.VideoWriter('face detection4.avi',fourcc,20.0,(640,480))
time.sleep(1)

while cap.isOpened():
    ret, frame= cap.read()
    height, width, ch = frame.shape

    blob = cv2.dnn.blobFromImage(frame, 1 / 255, (320, 320), (0, 0, 0), swapRB=True, crop=False)
    net.setInput(blob)

    outputs = net.forward(net.getUnconnectedOutLayersNames())
    boxes, confidences = [], []

    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > confThreshold and class_id == class_of_interest:
                center_x, center_y, w, h = map(int, detection[:4] * [width, height, width, height])
                x, y = center_x - w // 2, center_y - h // 2
                boxes.append([x, y, w, h])
                confidences.append(confidence)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, confThreshold, 0.4)
    font, colors = cv2.FONT_HERSHEY_PLAIN, np.random.uniform(0, 255, size=(len(boxes), 3))

    if len(indexes) > 0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label, color = str(classes[class_of_interest]), colors[i]
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, f"{label}", (x, y + 20), font, 2, (255, 255, 255), 2)

    for x,y,w,h in boxes:
        #sending coordinates to Arduino
        string='X{0:d}Y{1:d}'.format((x+w//2),(y+h//2))
        print(string)
        ArduinoSerial.write(string.encode('utf-8'))
        #plot the center of the face
        cv2.circle(frame,(x+w//2,y+h//2),2,(0,255,0),2)
        #plot the roi
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
    #plot the squared region in the center of the screen
    cv2.rectangle(frame,(640//2-30,480//2-30),
                 (640//2+30,480//2+30),
                  (255,255,255),3)
    #out.write(frame)
    cv2.imshow('img',frame)
    #cv2.imwrite('output_img.jpg',frame)
    '''for testing purpose
    read= str(ArduinoSerial.readline(ArduinoSerial.inWaiting()))
    time.sleep(0.05)
    print('data from arduino:'+read)
    '''
    # press q to Quit
    if cv2.waitKey(10)&0xFF== ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
