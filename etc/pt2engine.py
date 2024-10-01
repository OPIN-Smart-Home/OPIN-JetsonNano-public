from ultralytics import YOLO

# Input properties
frame_width = 640
frame_height = 640

# Load the YOLO model (TensorRT engine is optimized for Jetson Nano)
ptmodel = YOLO("yolov8n.pt")
ptmodel.export(format="engine", batch=8, int8=True, data="coco.yaml")
