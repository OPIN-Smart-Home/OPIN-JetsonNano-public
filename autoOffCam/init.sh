#!/bin/bash

sudo docker build --network=host -t auto-off-cam:latest .
sudo docker run --name ip_camera -t --ipc=host --runtime=nvidia --gpus all auto-off-cam:latest