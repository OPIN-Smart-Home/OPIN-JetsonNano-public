import os
import cv2
import math
import time
import torch
from ultralytics import YOLO

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

def get_gpu_info():
    if torch.cuda.is_available():
        gpu_name = torch.cuda.get_device_name(torch.cuda.current_device())
        total_memory = torch.cuda.get_device_properties(torch.cuda.current_device()).total_memory // (1024 ** 2)  # Convert bytes to MB
        used_memory = torch.cuda.memory_allocated(torch.cuda.current_device()) // (1024 ** 2)  # Convert bytes to MB

        return {
            "gpu_name": gpu_name,
            "mem_used": used_memory,
            "mem_total": total_memory
        }

# Load the URL
url = "rtsp://"
cap = cv2.VideoCapture(url)

# Get video properties
frame_width = 800
frame_height = 600
fps = cap.get(cv2.CAP_PROP_FPS)

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4
out = cv2.VideoWriter('rtsp.mp4', fourcc, fps, (frame_width, frame_height))

# Initialize variables for FPS calculation
frame_count = 0
fps_list = []

trtmodel_path = "yolov8n.engine"
if not os.path.isfile(trtmodel_path):
    ptmodel = YOLO("yolov8n.pt")
    ptmodel.export(format="engine")

model = YOLO("yolov8n.engine", task="detect")

while True:
    success, img = read_frame_with_retry(cap)
    if not success or img is None:
        print("Failed to capture image, attempting to reconnect...")
        cap.release()
        cap = start_video_capture(url)
        continue

    img = cv2.resize(img, (frame_width, frame_height))

    frame_count += 1
    start_frame_time = time.time()

    # Run object detection
    results = model(img, stream=True, classes=0)
    gpu_info = get_gpu_info()

    people_detected = 0

    for result in results:
        boxes = result.boxes  # Boxes object for bounding box outputs
        for box in boxes:
            # Bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            # Draw the bounding box
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # Confidence
            confidence = math.ceil((box.conf[0] * 100)) / 100

            # Print confidence
            print("Confidence --->", confidence)

            # Class name
            cls = int(box.cls[0])

            # Increment people counter
            if cls == 0:  # Assuming class 0 represents a person
                people_detected += 1

            # Draw the class name and confidence on the frame
            text = f'Person {confidence:.2f}'
            cv2.putText(img, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Calculate FPS
    end_frame_time = time.time()
    fps = 1.0 / (end_frame_time - start_frame_time)
    fps_list.append(fps)

    # Draw FPS on the image
    fps_text = f"FPS: {fps:.2f}"
    print(fps_text)
    cv2.putText(img, fps_text, (frame_width-200, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Draw Jetson info on the image
    gpu_info_text = f'{gpu_info["gpu_name"]}  {gpu_info["mem_used"]}/{gpu_info["mem_total"]}MB'
    print(gpu_info_text)
    cv2.putText(img, gpu_info_text, (frame_width//2, frame_height-30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Ensure img is valid before showing it
    if img is not None and img.size > 0:
        out.write(img)  # Save the frame to the video file
        cv2.imshow('Result', img)
    else:
        print("Error: Captured image is invalid")

    if cv2.waitKey(1) == ord('q'):
        break

# Release resources
cap.release()
out.release()  # Release the VideoWriter
cv2.destroyAllWindows()

# Calculate the average FPS across the video
average_fps = sum(fps_list) / len(fps_list)
print(f"Average FPS: {average_fps:.2f}")
