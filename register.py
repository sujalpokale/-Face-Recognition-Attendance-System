import cv2 
import numpy as np
import face_recognition
import sqlite3
import pickle

def register_user():
    video_capture = cv2.VideoCapture(0)
    name = input("Enter your name: ")
    
    print("Capturing your face. Please look at the camera.")
    while True:
        ret, frame = video_capture.read()
        if not ret:
            continue
        rgb_frame = frame[:,:,::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        
        if face_locations:
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)[0]
            conn = sqlite3.connect('attendance.db')
            c = conn.cursor()
            encoding_blob = pickle.dumps(face_encodings)
            c.execute("INSERT INTO users (name, encoding) VALUES (?, ?)", (name, encoding_blob))
            conn.commit()
            conn.close()
            print(f"User {name} registered successfully!")
            break
    
        cv2.imshow("Register Face",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
             break
    video_capture.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    register_user()
