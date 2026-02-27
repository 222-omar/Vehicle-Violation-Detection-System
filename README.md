Vehicle Speed Detection and Traffic Violation System
Overview

This project is a real-time vehicle speed detection and traffic violation monitoring system built using computer vision and artificial intelligence techniques. The system processes video input, detects vehicles, tracks their movement across predefined lines, calculates their speed, and identifies traffic violations when the speed exceeds a specified threshold.

Unlike traditional monitoring systems, this solution integrates object detection, speed estimation, optical character recognition (OCR), vehicle attribute analysis, and AI-powered violation reporting using the Gemini API.

The final output is presented through an interactive Streamlit dashboard that displays only violating vehicles in a structured database table.

Features

Real-time vehicle detection using YOLOv8

Multi-object tracking

Speed estimation based on distance and time between two reference lines

License plate extraction using OCR

Vehicle color and model estimation

Violation detection (speed > predefined limit)

AI-generated violation report using Gemini API

MySQL database integration

Interactive Streamlit dashboard

Multi-video support with custom detection lines

System Architecture

The system consists of the following components:

1. Object Detection

YOLOv8 is used to detect vehicles in each video frame. Bounding boxes are generated for each detected vehicle.

2. Object Tracking

Detected vehicles are assigned unique IDs to track their movement across frames.

3. Speed Estimation

Each video has two predefined reference lines. When a tracked vehicle crosses the first line, a timestamp is recorded. When it crosses the second line, another timestamp is captured.

Speed is calculated using:

Speed = Distance / Time

If:
Speed > 30 km/h (configurable threshold)

The vehicle is marked as a violator.

4. License Plate Recognition

OCR is applied to the detected plate region to extract the vehicle number.

5. Vehicle Attribute Extraction

The system estimates:

Vehicle color

Vehicle model (if classifier available)

6. Gemini API Integration

When a violation is detected, the system sends structured vehicle data to the Gemini API.
Gemini generates a formatted violation report including:

Vehicle number

Estimated speed

Time of violation

Vehicle description

7. Database Storage

Violation data is stored in a MySQL database including:

Vehicle ID

Plate number

Speed

Color

Model

Video source

Timestamp

8. Streamlit Dashboard

The dashboard allows:

Selecting between multiple videos

Running detection

Displaying only violating vehicles

Viewing violation records in a structured table

Project Structure
project/
│
├── app.py                  # Streamlit dashboard
├── speed_estimator.py      # Speed calculation logic
├── detector.py             # YOLO detection logic
├── ocr_module.py           # License plate recognition
├── gemini_report.py        # Gemini API integration
├── database.py             # MySQL connection and queries
├── video_lines.py          # Detection line coordinates
├── models/                 # YOLO and classification models
└── requirements.txt
Technologies Used

Python

OpenCV

YOLOv8

EasyOCR / Tesseract

MySQL

Streamlit

Gemini API

NumPy

Pandas

Installation
1. Clone the repository
git clone https://github.com/your-username/vehicle-speed-detection.git
cd vehicle-speed-detection
2. Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3. Install dependencies
pip install -r requirements.txt
4. Configure Environment Variables

Create a .env file and add:

GEMINI_API_KEY=your_api_key_here
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=traffic_system
Running the Application

To start the Streamlit dashboard:

streamlit run app.py

Then open the browser at:

http://localhost:8501
Multi-Video Support

Each video has custom detection lines defined in:

video_lines.py

Example:

"video1.mp4": [(1527, 97), (2, 71)]

This allows different camera angles and road layouts to be handled independently.

Database Schema

Example table structure:

CREATE TABLE violations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    plate_number VARCHAR(50),
    speed FLOAT,
    color VARCHAR(50),
    model VARCHAR(100),
    video_source VARCHAR(100),
    violation_time DATETIME
);
Future Improvements

Real-time live camera support

Automated fine calculation

SMS or email notification system

Cloud deployment

Improved plate detection accuracy

Edge device optimization

Analytics dashboard for violation trends

Limitations

Speed accuracy depends on correct distance calibration

OCR performance depends on lighting and plate visibility

Model accuracy may vary depending on camera angle

System currently optimized for controlled video input

Conclusion

This project demonstrates a complete AI-powered traffic monitoring pipeline integrating computer vision, tracking, database systems, and generative AI reporting.

It is designed not only as a technical implementation but as a potential real-world product foundation for smart traffic systems and automated law enforcement solutions.
