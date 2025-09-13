import cv2 
import face_recognition
import sqlite3
import pickle
from datetime import datetime
import numpy as np

def mark_attendance():
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    c.execute("SELECT id, name, encoding FROM users")
    rows = c.fetchall()
    conn.close()
    
    known_face_encodings = []
    face_ids = []
    known_face_names = []
    
    for row in rows:
        face_ids.append(row[0])
        known_face_names.append(row[1])
        known_face_encodings.append(pickle.loads(row[2]))
    
    video_capture = cv2.VideoCapture(0)
    
    print("Starting attendance system. Press 'q' to quit.")
    
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        rgd_frame = frame[:,:,::-1]
        face_locations = face_recognition.face_locations(rgd_frame)
        face_encodings = face_recognition.face_encodings(rgd_frame, face_locations)
        
        for face_encoding, face_locations in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding,tolerance=0.5)
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            name = "Unknown"
            
            if True in matches:
                match_index = matches.index(True)
                name = known_face_names[match_index]
                face_id = face_ids[match_index]
                
                conn = sqlite3.connect('attendance.db')
                c = conn.cursor()
                now = datetime.now()
                date = now.strftime("%Y-%m-%d")
                time = now.strftime("%H:%M:%S")
                c.execute("INSERT INTO attendance (user_id, date, time) VALUES (?, ?, ?)", (face_id, date, time))
                conn.commit()
                conn.close()
                print(f"Attendance marked for {name} at {time} on {date}")
                
            top, right, bottom, left = face_locations
            cv2.rectangle(frame, (left ,top), (right,bottom), (0,255,0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
        
        cv2.imshow("Attendance System", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    mark_attendance()               

            