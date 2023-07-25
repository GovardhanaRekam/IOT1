import cv2
import serial

face_cascade = cv2.CascadeClassifier('haar_face.xml')

cap = cv2.VideoCapture(0)

# Open the serial port.
# COM3 is used here, you need to replace it with your port
# 9600 is the baud rate and should match with the one on Arduino code
ser = serial.Serial('/dev/ttyUSB0', 9600)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    if(len(faces) !=0):
    	for (x,y,w,h) in faces:
        	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
        # If a face is detected, send a command to the Arduino
        	ser.write(b'1')  # send '1' to Arduino
    else:
    	ser.write(b'0')
    cv2.imshow('img', img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

