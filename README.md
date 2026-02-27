# Vehicle Speed Detection and Traffic Violation System

## Overview

This project is a real-time vehicle speed detection and traffic violation monitoring system built using computer vision and artificial intelligence techniques.

The system processes video input, detects vehicles, tracks their movement across predefined lines, calculates their speed, and identifies violations when the speed exceeds a configured threshold.

The project integrates object detection, speed estimation, OCR, vehicle attribute extraction, database storage, and AI-generated violation reports using the Gemini API.

The final output is presented through an interactive Streamlit dashboard that displays only violating vehicles in a structured table.

---

## Features

- Real-time vehicle detection using YOLOv8
- Multi-object tracking
- Speed estimation using two reference lines
- License plate recognition (OCR)
- Vehicle color and model estimation
- Violation detection (speed > threshold)
- AI-generated violation report using Gemini API
- MySQL database integration
- Streamlit dashboard
- Multi-video support with custom detection lines

---

## System Architecture

### 1. Object Detection
YOLOv8 detects vehicles in each video frame and generates bounding boxes.

### 2. Object Tracking
Each detected vehicle is assigned a unique ID to track it across frames.

### 3. Speed Estimation

Each video contains two predefined reference lines.

When a vehicle crosses:
- Line 1 → Start timestamp is recorded.
- Line 2 → End timestamp is recorded.

Speed is calculated using:

The vehicle is marked as a violator.

---

### 4. License Plate Recognition

OCR is applied to extract the license plate number from the detected plate region.

---

### 5. Vehicle Attribute Extraction

The system estimates:
- Vehicle color
- Vehicle model (if classifier is available)

---

### 6. Gemini API Integration

When a violation is detected, structured vehicle data is sent to Gemini API.

Gemini generates a formatted violation report including:
- Plate number
- Estimated speed
- Time of violation
- Vehicle description

---

### 7. Database Storage

Violation data is stored in MySQL:

- Plate number
- Speed
- Color
- Model
- Video source
- Timestamp

---

### 8. Streamlit Dashboard

The dashboard allows:
- Selecting between multiple videos
- Running detection
- Displaying only violating vehicles
- Viewing violation records in a structured table

---


---

## Technologies Used

- Python
- OpenCV
- YOLOv8
- EasyOCR / Tesseract
- MySQL
- Streamlit
- Gemini API
- NumPy
- Pandas

---

## Installation

### 1. Clone the Repository

### 2. Create Virtual Environment
