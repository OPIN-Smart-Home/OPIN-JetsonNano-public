import sys
import cv2
import math
import time
from ultralytics import YOLO
from firebase_admin import credentials, initialize_app, db

# Initialize Firebase with the provided credentials
cred = credentials.Certificate("/ultralytics/serviceAccountKey.json")
firebase = initialize_app(cred, {
    'databaseURL': 'https://[URL].firebasedatabase.app/'
})

# Function to create and start video capture
def start_video_capture(url):
    cap = cv2.VideoCapture(url)
    if not cap.isOpened():
        print("Error: Could not open video stream")
    return cap

# Function to read frame with retries
def read_frame_with_retry(cap, retries=5, delay=2):
    for i in range(retries):
        success, img = cap.read()
        if success:
            return success, img
        time.sleep(delay)
        print(f"Retrying to read frame {i+1}/{retries}...")
    return False, None

# Load the URL
url = sys.argv[1]
path = sys.argv[2]
cap = cv2.VideoCapture(url)

# Device UID
with open('/ultralytics/uid.txt', 'r') as file:
    access_id = file.read().strip()

# Get a reference to the Firebase Realtime Database service
ref = db.reference('/' + path)

# Get video properties
frame_width = 640
frame_height = 640
ori_fps = cap.get(cv2.CAP_PROP_FPS)

# Initialize variables for FPS calculation
frame_count = 0
fps_list = []

trtmodel_path = "yolov8n.engine"
model = YOLO(trtmodel_path, task="detect")

failed = 0
while True:
    start_frame_time = time.time()
    success, img = read_frame_with_retry(cap)
    if not success or img is None:
        print("Failed to capture image, attempting to reconnect...")
        cap.release()
        cap = start_video_capture(url)
        failed += 1
        if failed == 3:
            exit()
        continue

    failed = 0
    frame_count += 1
    if(frame_count % 10 == 0):
        img = cv2.resize(img, (frame_width, frame_height))

        # Run object detection
        results = model(img, classes=0)

        people_detected = 0
        for result in results:
            boxes = result.boxes  # Boxes object for bounding box outputs
            for box in boxes:
                # Bounding box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                # Confidence
                confidence = math.ceil((box.conf[0] * 100)) / 100

                # Print confidence
                print("Confidence --->", confidence)

                people_detected += 1
        ref.set(people_detected)

    # Calculate FPS
    end_frame_time = time.time()
    fps = 1.0 / (end_frame_time - start_frame_time)
    print(f"FPS: {fps:.2f}")
    fps_list.append(fps)