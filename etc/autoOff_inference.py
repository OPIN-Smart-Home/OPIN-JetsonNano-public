import os
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
url = "rtsp://"
cap = cv2.VideoCapture(url)

# Get a reference to the Firebase Realtime Database service
ref = db.reference('/OPIN_xxxxxxxxxxxxxxxx/cctv-cam')

# Get video properties
frame_width = 640
frame_height = 640
ori_fps = cap.get(cv2.CAP_PROP_FPS)

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4
out = cv2.VideoWriter('inference.mp4', fourcc, ori_fps, (frame_width, frame_height))

# Initialize variables for FPS calculation
frame_count = 0
fps_list = []

trtmodel_path = "yolov8n.engine"
if not os.path.isfile(trtmodel_path):
    ptmodel = YOLO("yolov8n.pt")
    ptmodel.export(format="engine")

model = YOLO("yolov8n.engine", task="detect")

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
            break
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

                # Draw the bounding box
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 2)

                # Confidence
                confidence = math.ceil((box.conf[0] * 100)) / 100

                # Print confidence
                print("Confidence --->", confidence)

                people_detected += 1

                # Draw the class name and confidence on the frame
                text = f'Person {confidence:.2f}'
                cv2.putText(img, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

        ref.set(people_detected)

    # Calculate FPS
    end_frame_time = time.time()
    fps = 1.0 / (end_frame_time - start_frame_time)
    fps_list.append(fps)

    # Draw FPS on the image
    fps_text = f"FPS: {fps:.2f}"
    print(fps_text)
    cv2.putText(img, fps_text, (frame_width-150, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    # Ensure img is valid before showing it
    if img is not None and img.size > 0:
        cv2.imshow('Result', img)
    else:
        print("Error: Captured image is invalid")

    if cv2.waitKey(1) == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

# Calculate the average FPS across the video
average_fps = sum(fps_list) / len(fps_list)
print(f"Average FPS: {average_fps:.2f}")
