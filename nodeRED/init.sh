#!/bin/bash

sudo docker build --network=host -t opin:latest .
docker run -d --restart=always --name opin -p 1880:1880 -p 5432:5432 -v /var/run/docker.sock:/var/run/docker.sock opin:latest