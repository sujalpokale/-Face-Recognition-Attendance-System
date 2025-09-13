# Face-Recognition-Attendance-System

## 📝 Overview

The **Face Recognition Attendance System** is a Python-based application designed to automate the process of recording attendance using facial recognition technology. This system leverages the `face_recognition` library and OpenCV to identify individuals and mark their attendance in real-time. It's ideal for educational institutions, workplaces, or any environment where efficient and accurate attendance tracking is required.

---

## 🚀 Features

- **User Registration**: Register new users by capturing their facial images.
- **Real-Time Attendance**: Automatically mark attendance by recognizing faces through the webcam.
- **Attendance History**: View and manage attendance records with timestamps.
- **Flask Web Interface**: User-friendly web interface for interaction.
- **SQLite Database**: Lightweight database to store user and attendance data.

---

## 📦 Installation

### Prerequisites

Ensure you have Python 3.7+ installed. It's recommended to use a virtual environment.

```bash
# Create and activate a virtual environment
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```
### 🧪 Usage
1. Register Users
Navigate to the Register page.
Enter the user's name and click "Register".
The system will capture the user's face and store the encoding for future recognition.

2. Mark Attendance
Go to the Attendance page.
The system will use your webcam to detect and recognize faces.
Upon successful recognition, attendance will be recorded with the current timestamp.

3. View Attendance Records
Access the View Attendance page.
Browse through the list of recorded attendance entries.

## 🛠 Technologies Used

- Python
- OpenCV
- face_recognition
- Tkinter
- SQLite
- NumPy
- Pillow

