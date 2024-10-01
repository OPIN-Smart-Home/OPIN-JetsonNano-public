import cv2
from ultralytics import YOLO

img = cv2.imread("/ultralytics/sample.jpeg")

# # Load a YOLOv8n PyTorch model
# model = YOLO("yolov8n.pt")

# # Export the model
# model.export(format="engine")  # creates 'yolov8n.engine'

# Load the exported TensorRT model
trt_model = YOLO("yolov8n.engine")

# Run inference
results = trt_model(img)

print(results)

