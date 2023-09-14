'''import cv2
import numpy as np
import os
import face_recognition
import serial
import time
import requests
from datetime import datetime, timedelta
import threading
from flask import Flask, render_template, Response, stream_with_context

# Flask Setup
app = Flask(__name__)

def generate():
    while True:
        with lock:
            frame = img.copy()
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(stream_with_context(generate()), content_type='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('app.html')

def run_flask_app():
    app.run(host='0.0.0.0', port=5000)

# Face Recognition Setup
ser = serial.Serial('/dev/ttyUSB0', 9600)
path = r'/home/amma/Desktop/img'
images = []
classNames = []
myList = os.listdir(path)
last_known_time = None
last_unknown_time = None
last_known_person = ""

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
threshold = 0.6
lock = threading.Lock()
img = None

def sendToThingSpeak(name, timestamp):
    url = "http://api.thingspeak.com/update"
    data = {
        "api_key": "C7QLG8IFLF1QA4S6",
        "field1": name,
        "field2": timestamp
    }
    response = requests.post(url, data=data)
    print(response.text)

def process_faces():
    global img, last_known_time, last_unknown_time, last_known_person
    while True:
        with lock:
            frame = img.copy() if img is not None else None

        if frame is not None:
            imgS = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                matchIndex = np.argmin(faceDis)

                name = 'Unknown'
                if matches[matchIndex] and faceDis[matchIndex] < threshold:
                    name = classNames[matchIndex].upper()

                if name != 'Unknown':
                    ser.write(b"1")
                    time.sleep(10)
                else:
                    ser.write(b"0")

                
                # Sending data logic
                if name != 'Unknown':
                    if (last_known_time is None or datetime.now() - last_known_time > timedelta(minutes=10)) and name != last_known_person:
                        last_known_time = datetime.now()
                        last_known_person = name
                        sendToThingSpeak(name, str(last_known_time))
                        print(name)  # Print the name of the known person
               

                else:  # The detected person is 'Unknown'
                    if (name == 'Unknown') and (last_unknown_time is None or datetime.now() - last_unknown_time > timedelta(minutes=2)):
                        last_unknown_time = datetime.now()
                        message = name + " detected, let's stream" 
                        sendToThingSpeak(message, str(last_unknown_time))

                
                if name != 'Unknown' and (last_known_time is None or datetime.now() - last_known_time > timedelta(minutes=10)) and name != last_known_person:
                    last_known_time = datetime.now()
                    last_known_person = name
                    sendToThingSpeak(name, str(last_known_time))
                elif name == 'Unknown' and (last_unknown_time is None or datetime.now() - last_unknown_time > timedelta(minutes=2)):
                    last_unknown_time = datetime.now()
                    sendToThingSpeak(name, str(last_unknown_time))


        time.sleep(0.1)

if __name__ == '__main__':
    # Start Flask app and face processing in separate threads
    thread_app = threading.Thread(target=run_flask_app)
    thread_faces = threading.Thread(target=process_faces, daemon=True)

    thread_app.start()
    thread_faces.start()

    # The main while loop for displaying the frames
    while True:
        success, img = cap.read()
        if not success:
            break

        with lock:
            frame_to_show = img.copy()

        if frame_to_show is not None:
        	imgS = cv2.resize(frame_to_show, (0, 0), None, 0.25, 0.25)
        	imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        	facesCurFrame = face_recognition.face_locations(imgS)
        	encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDis)

            name = 'Unknown'
            if matches[matchIndex] and faceDis[matchIndex] < threshold:
                name = classNames[matchIndex].upper()

            # Draw rectangle and put label
            top, right, bottom, left = faceLoc
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            cv2.rectangle(frame_to_show, (left, top), (right, bottom), (255, 0, 0), 2)
            cv2.putText(frame_to_show, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

        
        cv2.imshow('Webcam', frame_to_show)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
'''
import cv2
import numpy as np
import os
import face_recognition
import serial
import time
import requests
from datetime import datetime, timedelta
import threading
from flask import Flask, render_template, Response, stream_with_context

# Flask Setup
app = Flask(__name__)

def generate():
    while True:
        with lock:
            frame = img.copy()
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(stream_with_context(generate()), content_type='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('app.html')

def run_flask_app():
    app.run(host='0.0.0.0', port=8000)

# Face Recognition Setup
ser = serial.Serial('/dev/ttyUSB0', 9600)
path = r'/home/amma/Desktop/img'
images = []
classNames = []
myList = os.listdir(path)
last_known_time = None
last_unknown_time = None
last_known_person = ""

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
threshold = 0.5
lock = threading.Lock()
img = None

def sendToThingSpeak(name, timestamp):
    url = "http://api.thingspeak.com/update"
    data = {
        "api_key": "C7QLG8IFLF1QA4S6",
        "field1": name,
        "field2": timestamp
    }
    response = requests.post(url, data=data)
    print(response.text)

def process_faces():
    global img, last_known_time, last_unknown_time, last_known_person
    while True:
        with lock:
            frame = img.copy() if img is not None else None

        if frame is not None:
            imgS = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                matchIndex = np.argmin(faceDis)

                name = 'Unknown'
                if matches[matchIndex] and faceDis[matchIndex] < threshold:
                    name = classNames[matchIndex].upper()

                if name != 'Unknown':
                    ser.write(b"1")
                    time.sleep(10)
                else:
                    ser.write(b"0")

                # Sending data logic
                if name != 'Unknown':
                    if (last_known_time is None or datetime.now() - last_known_time > timedelta(minutes=10)) and name != last_known_person:
                        last_known_time = datetime.now()
                        last_known_person = name
                        sendToThingSpeak(name, str(last_known_time))
                        print(name)  # Print the name of the known person
                else:  # The detected person is 'Unknown'
                    if (name == 'Unknown') and (last_unknown_time is None or datetime.now() - last_unknown_time > timedelta(minutes=2)):
                        last_unknown_time = datetime.now()
                        message = name + " detected, let's stream" 
                        sendToThingSpeak(message, str(last_unknown_time))

        time.sleep(0.1)

if __name__ == '__main__':
    # Start Flask app and face processing in separate threads
    thread_app = threading.Thread(target=run_flask_app)
    thread_faces = threading.Thread(target=process_faces, daemon=True)

    thread_app.start()
    thread_faces.start()

    # The main while loop for displaying the frames
    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        if not success:
            break

        with lock:
            frame_to_show = img.copy()

        if frame_to_show is not None:
            imgS = cv2.resize(frame_to_show, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDis)

            name = 'Unknown'
            if matches[matchIndex] and faceDis[matchIndex] < threshold:
                name = classNames[matchIndex].upper()

            # Draw rectangle and put label
            top, right, bottom, left = faceLoc
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            cv2.rectangle(frame_to_show, (left, top), (right, bottom), (255, 0, 0), 2)
            cv2.putText(frame_to_show, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

        cv2.imshow('Webcam', frame_to_show)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

