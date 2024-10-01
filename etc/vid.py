import os
import cv2
import math
import time
from ultralytics import YOLO

# Load the video file
vid = "sample.mp4"
cap = cv2.VideoCapture(vid)

# Get video properties
frame_width = 640
frame_height = 640
ori_fps = cap.get(cv2.CAP_PROP_FPS)

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4
out = cv2.VideoWriter('output_best.mp4', fourcc, ori_fps, (frame_width, frame_height))

# Initialize variables for FPS calculation
frame_count = 0
fps_list = []

trtmodel_path = "best.engine"
if not os.path.isfile(trtmodel_path):
    ptmodel = YOLO("best.pt")
    ptmodel.export(format="engine")

model = YOLO("best.engine", task="detect")

while True:
    ret, img = cap.read()
    if not ret:
        break

    img = cv2.resize(img, (frame_width, frame_height))

    frame_count += 1
    start_frame_time = time.time()

    # Run object detection
    results = model(img)

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

            # Draw the class name and confidence on the frame
            text = f'Person {confidence:.2f}'
            cv2.putText(img, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Calculate FPS
    end_frame_time = time.time()
    fps = 1.0 / (end_frame_time - start_frame_time)
    fps_list.append(fps)

    # Draw FPS on the image
    fps_text = f"Original Video FPS: {ori_fps}"
    print(fps_text)
    fps_text = f"FPS: {fps:.2f}"
    print(fps_text)
    cv2.putText(img, fps_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

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
