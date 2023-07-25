import pandas as pd
import cv2
import numpy as np
import os
from datetime import datetime
import face_recognition
import serial

# initialize serial port
ser = serial.Serial('/dev/ttyUSB0', 9600)
#ser = serial.Serial('COM3', 9600)  use this for windows

path = r'replace your own path images'


images = []
classNames = []
myList = os.listdir(path)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown = findEncodings(images)

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    recognized_faces = False

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            recognized_faces = True

    # Send command to Arduino
    if recognized_faces:
        ser.write(b'1') # signal to turn LED on
    else:
        ser.write(b'0') # signal to turn LED off

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
'''
This code integrates face recognition, OpenCV, and Arduino to build a face-detection system that triggers a light when a known face is identified. The program starts by capturing images from a webcam using OpenCV. It then utilizes the face_recognition library to compare the live feed with a set of known images stored in a specified directory. When a match is found, it sends a signal to an Arduino microcontroller, which in turn triggers the LED to turn ON. If the detected face is not found in the stored images or no face is detected, the LED remains OFF. The solution leverages Python's powerful libraries and the interoperability of Python with Arduino to create a simple, interactive face-detection system.'''

