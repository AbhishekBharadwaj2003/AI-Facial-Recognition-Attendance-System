<div align="center">

# 🎯 AI-Based Facial Recognition Attendance System

### AI-Powered Attendance Management using Computer Vision, InsightFace & Streamlit

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge&logo=streamlit)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge&logo=sqlite)

<img src="screenshots/dashboard.png" width="1000">

</div>

---

# 📖 Overview

The **AI-Based Facial Recognition Attendance System** is an end-to-end computer vision application that automates attendance using real-time face recognition.

The application captures live video from a webcam, detects faces, generates facial embeddings using **InsightFace**, recognizes registered students using **Cosine Similarity**, automatically marks attendance, stores records in a **SQLite database**, and provides a beautiful **Streamlit dashboard** for analytics and management.

---

# ✨ Features

- 👤 Student Registration
- 📸 Face Dataset Collection
- 🧠 AI Face Recognition using InsightFace
- 🎥 Real-Time Face Detection
- ✅ Automatic Attendance Marking
- 🗄 SQLite Database Integration
- 📊 Interactive Analytics Dashboard
- 📈 Attendance Statistics
- 👥 Student Management
- 📜 Attendance History
- 📥 Export Attendance to Excel
- 🚨 Unknown Face Logger
- 🏗 Modular Project Structure

---

# 🛠 Tech Stack

### Programming Language

- Python

### Computer Vision

- OpenCV
- InsightFace
- ONNX Runtime

### Machine Learning

- Cosine Similarity
- NumPy
- Scikit-learn

### Dashboard

- Streamlit
- Plotly
- Pandas

### Database

- SQLite

### Excel Export

- OpenPyXL

---

# 📂 Project Structure

```text
AI-Based-Facial-Recognition-Attendance-System/

│
├── app.py
├── streamlit_app.py
├── register_student.py
├── generate_embeddings.py
├── export_attendance.py
├── requirements.txt
├── README.md
│
├── assets/
├── pages/
├── screenshots/
├── utils/
├── dataset/
├── database/
├── embeddings/
├── exports/
└── unknown_faces/
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/AbhishekBharadwaj2003/AI-Facial-Recognition-Attendance-System.git

cd AI-Facial-Recognition-Attendance-System
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

## Generate Face Embeddings

```bash
python generate_embeddings.py
```

## Register Student

```bash
python register_student.py
```

## Start Live Face Recognition

```bash
python app.py
```

## Launch Streamlit Dashboard

```bash
python -m streamlit run streamlit_app.py
```

## Export Attendance

```bash
python export_attendance.py
```

---

# 🧠 System Workflow

```text
Student Registration
        │
        ▼
Capture Face Images
        │
        ▼
Generate Face Embeddings
        │
        ▼
Store Embeddings
        │
        ▼
Live Webcam Detection
        │
        ▼
Face Recognition
        │
        ▼
Attendance Marked
        │
        ▼
SQLite Database
        │
        ▼
Streamlit Dashboard
```

---

# 📸 Application Screenshots

## 📊 Dashboard

<p align="center">
<img src="screenshots/dashboard.png" width="900">
</p>

---

## 🎥 Live Recognition

<p align="center">
<img src="screenshots/live_recognition.png" width="900">
</p>

---

## 📈 Attendance Analytics

<p align="center">
<img src="screenshots/analytics.png" width="900">
</p>

---

## 👤 Register Student

<p align="center">
<img src="screenshots/register_student.png" width="900">
</p>

---

## 👥 Students Page

<p align="center">
<img src="screenshots/students_page.png" width="900">
</p>

---

## 📥 Download Attendance

<p align="center">
<img src="screenshots/download_page.png" width="900">
</p>

---

## 🕒 Attendance History

<p align="center">
<img src="screenshots/attendance_history.png" width="900">
</p>

---

# 🎯 Learning Outcomes

This project demonstrates practical experience with:

- Computer Vision
- Face Recognition
- Feature Embeddings
- Cosine Similarity
- Image Processing
- Real-Time Video Processing
- SQLite Database Design
- Streamlit Dashboard Development
- Modular Python Application Design

---

# 🚀 Future Improvements

- Face Anti-Spoofing
- Multi-Camera Support
- Live Camera Feed inside Streamlit
- REST API Integration
- Cloud Database Support
- Docker Deployment
- User Authentication
- Mobile Application

---

# 👨‍💻 Author

## Abhishek Bharadwaj

📧 **Email**

abhishekbharadwaj120@gmail.com

🔗 **LinkedIn**

https://www.linkedin.com/in/abhishek-bharadwaj-63b075317/

💻 **GitHub**

https://github.com/AbhishekBharadwaj2003

---

<div align="center">

### ⭐ If you found this project helpful, consider giving it a Star!

</div>
