import streamlit as st
import os
import cv2
import time
from speed_estimator import SpeedEstimator
from regions import video_lines
import mysql.connector
from datetime import datetime
from PIL import Image

# Database Configuration
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "vehicle_data"
}

# Function to fetch violators
def fetch_violators():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM vehicle_records WHERE speed > 50 ORDER BY date_time DESC")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    except Exception as e:
        st.error(f"❌ Error fetching data: {e}")
        return []

# Page configuration
st.set_page_config(page_title="🚗 Vehicle Violations", layout="wide")

# Set your logo path here
logo_path = "logo.jpg"  

# Layout: Logo on right, title center
cols = st.columns([1, 5, 1])  

# Right column (logo)
with cols[0]:
    if os.path.exists(logo_path):
        logo = Image.open(logo_path)
        st.image(logo, width=150)
    else:
        st.warning("⚠️ Logo not found.")

# Middle column (title)
with cols[1]:
    st.markdown("<h1 style='text-align: center;'>📽️ Vehicle Violation Detection System</h1>", unsafe_allow_html=True)



# Video selection
st.sidebar.title("📂 Video Options")
video_options = list(video_lines.keys())
selected_video = st.sidebar.selectbox("Select a video", video_options)

# ------------- Run Detection Button -------------
if selected_video and st.sidebar.button("▶️ Run Detection"):
    video_path = os.path.join("videos", selected_video)
    region = video_lines[selected_video]

    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps == 0:
        st.error("❌ Could not read video FPS.")
        st.stop()
    frame_delay = 1.0 / fps

    speed_obj = SpeedEstimator(region=region, model="yolo12s.pt", line_width=2)

    st.info("🔄 Processing... Video is playing below")
    video_placeholder = st.empty()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (640, 360))
        processed_frame = speed_obj.estimate_speed(frame)
        processed_frame = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)

        video_placeholder.image(processed_frame, channels="RGB", use_container_width=False)
        time.sleep(frame_delay)

    cap.release()
    st.success("✅ Video processed successfully!")

    # Show violators
    violators = fetch_violators()
    if violators:
        st.subheader("🚨 Violators Detected (Speed > 50 km/h)")
        st.dataframe(violators, use_container_width=True)
    else:
        st.info("✅ No violators detected in this video.")