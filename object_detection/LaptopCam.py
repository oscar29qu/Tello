import cv2
import threading
import os
import time
global frame



def mystream_pc():
    global frame
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame,(720,480))
        cv2.putText(frame,"Texto",(75,50),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,255),2) #font, font scale, color, thickness, line type
        cv2.imshow('Input', frame)
    
        c = cv2.waitKey(1)
        if c == 27: #Escape key
            break

    cap.release()
    cv2.destroyAllWindows()

b = threading.Thread(name='background', target=mystream_pc)
b.start()
