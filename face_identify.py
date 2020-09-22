import numpy as np
import cv2
import pyfirmata
import time

face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_alt2.xml')
#face_cascade = cv2.CascadeClassifier('cascades/haarcascade_profileface.xml')

cap = cv2.VideoCapture(0)

board = pyfirmata.Arduino('/dev/cu.usbmodem14101')
global pin9
iter8 = pyfirmata.util.Iterator(board)
iter8.start()

pin9 = board.get_pin('d:9:s')

def move_servo(angle):
    pin9.write(angle)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)
    #face = face_cascade2.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)
    for (x,y,w,h) in faces:
        if x < 200:
            print("out of frame! rotate CCW") # want to actually move motor here
            move_servo(10)
        elif x > 800:
            print("out of frame! rotate CW") # want to actually move motor here
            move_servo(10)
        else:
            print(x,y,w,h)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 5)
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
