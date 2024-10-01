# MODIFIED
# Ultralytics YOLO 🚀, AGPL-3.0 license
# Builds ultralytics/ultralytics:jetson-jetpack4 image on DockerHub https://hub.docker.com/r/ultralytics/ultralytics
# Supports JetPack4.x for YOLOv8 on Jetson Nano, TX2, Xavier NX, AGX Xavier

# Start FROM https://catalog.ngc.nvidia.com/orgs/nvidia/containers/l4t-cuda
FROM ultralytics/ultralytics:latest-jetson-jetpack4

# Create working directory
WORKDIR /ultralytics

# Install pip packages
RUN pip install firebase-admin

COPY . .
