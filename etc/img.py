import cv2
import math
import datetime
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model.cuda()
img = cv2.imread("sample2.jpg")
img = cv2.resize(img, (640, 640))

timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
print(f"\n=====\n[{timestamp}] START")

results = model(img)

timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
print(f"[{timestamp}] FINISH\n=====\n")

while True:
    for result in results:
        boxes = result.boxes  # Boxes object for bounding box outputs
        for box in boxes:
            # Bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # Confidence
            confidence = math.ceil((box.conf[0] * 100)) / 100
            print("Confidence --->", confidence)

            # Class name
            cls = int(box.cls[0])

            # Object details
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2

            # Draw bounding box and text on the image
            cv2.putText(img, 'Person', org, font, fontScale, color, thickness)
        
    #  Ensure img is valid before showing it
    if img is not None and img.size > 0:
        # img_resize = cv2.resize(img, (800, 600))
        cv2.imshow('Result', img)
    else:
        print("Error: Captured image is invalid")

    if cv2.waitKey(0) == ord('q'):
        break

cv2.destroyAllWindows()
