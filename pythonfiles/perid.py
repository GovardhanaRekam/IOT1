import os
import face_recognition
import cv2
import numpy as np
import serial

# Start serial communication
ser = serial.Serial('/dev/ttyUSB0', 9600)

# Load face encodings
known_face_encodings = []
known_face_names = []
image_folder = r'/home/rguktrkvalley/Desktop/img'  # Replace with your image folder path

image_filenames = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]

for image_filename in image_filenames:
    image = face_recognition.load_image_file(os.path.join(image_folder, image_filename))
    face_encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(face_encoding)
    known_face_names.append(image_filename.split('.')[0])  # Remove the extension from the filename

# Load the webcam source
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            ser.write('1'.encode())  # Send '1' when a known face is recognized

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
ser.close()

