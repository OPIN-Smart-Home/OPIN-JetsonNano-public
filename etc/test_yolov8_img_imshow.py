import cv2
import datetime
from ultralytics import YOLO

model = YOLO("yolov8n.engine")
img = cv2.imread("sample.jpeg")

timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
print(f"\n=====\n[{timestamp}] START")

results = model.predict(
        img,  # batch=8 of the same image
        verbose=False,
        device=0
    )

timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
print(f"[{timestamp}] FINISH\n=====\n")

#print(results)
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    result.show()  # display to screen
    result.save(filename="result.jpg")
