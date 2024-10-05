# Nvidia Jetson Nano as the Gateway for OPIN Smart Home System

![Jetson Nano](https://github.com/OPIN-Smart-Home/OPIN-JetsonNano-public/blob/main/asset/JetsonNano.png)

## Table of Contents
For Users
- [Introduction](#introduction)
- [Features](#features)
- [Peripherals](#peripherals)
- [User Guide](#user-guide)
- [Auto Off Feature](#auto-off-feature)

For Developers
- [Installation](#installation)
- [Device Manager System (Node-RED)](#device-manager-system-node-red)
- [Auto-Off System (Human Detection)](#auto-off-system-human-detection)
- [Limitations](#limitations)
- [Future Development](#future-development)

Additional Information
- [Further Information](#further-information)

 ---
 ---

# For Users
## Introduction
The Jetson Nano serves as the central gateway for the OPIN Smart Home system, acting as the brain that manages smart home devices and ensures efficient automation. Its primary tasks include monitoring and controlling connected devices such as smart lights, IP cameras, and smart locks. Additionally, the Jetson Nano leverages its powerful AI capabilities to run real-time human detection, which plays a crucial role in the system's automation.

Through human detection, the gateway ensures that devices such as lights and air conditioner are automatically turned off when no human presence is detected, optimizing energy usage and enhancing convenience for users. The Jetson Nano thus combines device management and intelligent automation to create a seamless and energy-efficient smart home experience.


## Features
1. **Centralized Device Management**  
    The Jetson Nano acts as the core hub, managing all connected smart devices such as lights, cameras, and locks. It provides seamless communication and control, ensuring all devices work together efficiently within the smart home ecosystem.

2. **AI-Powered Human Detection**  
    Leveraging its powerful GPU, the Jetson Nano runs real-time human detection algorithms, enabling automatic control of smart devices. For example, it can detect human presence and trigger actions like turning off lights or cameras when no one is in the room, helping to conserve energy.

3. **Auto-Off Functionality for Smart Devices**  
    Through its human detection capabilities, the Jetson Nano can automatically turn off devices such as lights, fans, or cameras when they are no longer needed, enhancing convenience and optimizing energy consumption.

4. **Scalability and Flexibility**  
    The Jetson Nano supports the addition of new devices and functionalities, making the OPIN Smart Home system flexible and scalable. Users can easily integrate additional smart devices without extensive configuration.

5. **Local Processing for Improved Performance**  
    By performing human detection and device management tasks locally on the Jetson Nano, the system reduces latency and increases reliability, minimizing the need for cloud-based processing.

6. **Customizable Automation Rules**  
    Users can set specific automation rules based on their preferences, such as turning off lights after a set time of inactivity or locking doors when no presence is detected, allowing for personalized smart home control.


## Peripherals
### Power Connection
- **Power Supply**: The Jetson Nano requires a 5V power supply. Connect the [power adapter](<https://images-cdn.ubuy.co.id/635295dbab2f2009a3160225-waveshare-power-supply-for-jetson.jpg>) to the barrel jack on the board. **Do not use the USB Type-C interface for power input.** Ensure that the power supply is sufficient (at least 2.5A) to support the Jetson Nano and any connected peripherals.

### HDMI Display Connection
- **HDMI Port**: Connect an HDMI cable from the Jetson Nano to a monitor or TV for visual output. This is necessary for initial setup or configuration changes. 

- **Connecting to a Laptop**: You can also connect the Jetson Nano to a laptop using a [video capture device](<https://specialist.co.id/cdn/shop/files/02_8ae3e938-18d9-46c5-832c-c1562cbc86dc_2048x2048.jpg?v=1691553964>). Connect the HDMI output from the Jetson Nano to the video capture device, and then connect the capture device to a USB port on the laptop. Use software like [OBS (Open Broadcaster Software)](<https://obsproject.com/download>) to display the output. In OBS, add a new source by selecting ``Video Capture Device`` and choose the video capture device as the source, typically labeled as ``USB Video``.

### USB Mouse and Keyboard
- **Input Devices**: Connect a USB mouse and keyboard to the available USB ports for navigation and input during the setup process.

### Power Button
- **Power On**: The Jetson Nano, equipped with a Waveshare casing, has a dedicated power button. To turn it on, simply press the button once (no need to hold it). The power button LED will illuminate to indicate that it is on. It takes around 30 seconds to 1 minute to boot up and be ready for use.

- **Power Off**: To turn it off, press the power button once again. It will take approximately 30 seconds to 1 minute to shut down completely, and the power button LED will turn off to indicate that it is powered down.
> **Note**: Always ensure that you safely shut down the Jetson Nano before unplugging it to avoid potential data corruption or system issues.

### Reset Button
- **Resetting the Device**: The Jetson Nano features a physical reset button, If you need to reset the device, simply press the reset button to reboot it. This can be useful in situations where the device becomes unresponsive.

### Micro SD / TF Card Port
- **Storage**: The Jetson Nano has a micro SD card slot for storage. It is essential for the operating system and any applications you wish to run on the device.
> **Warning**: Never remove the micro SD card while the Jetson Nano is powered on. Doing so can result in data corruption or loss, and may cause the device to become unresponsive.


## User Guide
Follow these steps to get started with setting up and using your smart home devices. This section will help you understand how to effectively use and control your devices with the OPIN Smart Home system.
### Setting Up the Gateway
1. **Connect the Jetson Nano to Power, Display, Mouse, and Keyboard**  
    Plug the Jetson Nano into a power source, and connect it to an HDMI display, a USB mouse, and a USB keyboard to set up the Wi-Fi connection.
    > **Note:** The display, mouse, and keyboard are only required for the first-time setup or when you need to change the Wi-Fi connection. After the initial setup, the Jetson Nano can operate without these peripherals.

2. **Set Up Wi-Fi**  
    Once the Jetson Nano boots up, navigate to the Wi-Fi settings on the desktop interface. Select your home Wi-Fi network and enter the password to connect. 

3. **Optional: Ethernet Connection**  
    If preferred, you can connect the Jetson Nano to the network via an Ethernet cable for a stable connection.

4. **Install the OPIN Mobile Application**  
    Download and install the OPIN application from the official repository, feel free to contact [me](#further-information). Follow the installation instructions provided within the app.

5. **Input the Gateway UID**  
    Open the OPIN application and input the gateway UID to connect to the services. This allows the application to communicate with the Jetson Nano and manage the smart home devices.
    
    Format: ``OPIN_[16DigitCharacters]``

### Troubleshooting
- **Check Connection**: Ensure that the devices and the Jetson Nano are on the same local network, and confirm that the Jetson Nano is connected to the internet.
- **Rebooting Devices**: Try rebooting the Jetson Nano through ``RESET`` button.
- **Re-adding Devices**: If a device is consistently unresponsive, you may need to remove it from the dashboard and add it again.


## Auto Off Feature
The OPIN SmartLamp includes an **Auto Off** feature designed to enhance energy efficiency by automatically turning off the lamp when no one is detected in the room. This feature utilizes a single IP camera to monitor the room and determine occupancy.
### Requirements
To utilize the Auto Off feature, users need to provide the following information in the OPIN mobile app:
- **IP Address**: The local IP address of the connected IP camera.
- **RTSP Link**: The Real-Time Streaming Protocol (RTSP) link for the IP camera. This link allows the SmartLamp to access the camera's video stream for occupancy detection.
### IP Camera Compatibility
Any IP camera that supports RTSP can be used for the Auto Off feature. Ensure that the selected IP camera is properly configured and positioned to effectively monitor the area where the SmartLamp is located.
### Note
- Only one IP camera can be used for the Auto Off feature. 
- Properly configuring the IP address and RTSP link is essential for the successful operation of the Auto Off feature. Incorrect settings may prevent the SmartLamp from functioning as intended.
By leveraging the Auto Off feature, users can enjoy the convenience of smart devices while also promoting energy conservation in their homes.

---
---

# For Developers
This section provides guidelines for developers looking to contribute to the OPIN Smart Home system. It's recommended to pay attention on [For Users](#for-users) section.

## Installation
This section is intended for a new or freshly purchased Jetson Nano that has not yet been set up.
1. **Install Jetson Nano OS**
    - Download the Jetson Nano OS image from the [NVIDIA website](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit).
    - Follow the instructions provided to flash the OS onto a microSD card, 64GB or higher is recommended.
    - Insert the microSD card into the Jetson Nano and power it on to complete the OS setup.
    - Grant user all root access by add this line on ``/etc/sudoers``.
        ```bash
        [username] ALL=(ALL) NOPASSWD:ALL
        ```
    - Optional: Enable auto login in user setting

2. **Update and Upgrade OS**
    ```bash
    sudo apt-get update
    sudo apt-get upgrade
    sudo reboot
    ```
    This is the current os-release

    ![OS Release](https://github.com/OPIN-Smart-Home/OPIN-JetsonNano-public/blob/main/asset/os-release.jpg)

3. **Clone This Repository**
    ```bash
    cd
    git clone https://github.com/OPIN-Smart-Home/OPIN-JetsonNano-public.git
    cd OPIN-JetsonNano-public/
    ```

4. **Fan Configuration (Optional)**  
    To configure the fan, edit [``/fan/config.json``](https://github.com/OPIN-Smart-Home/OPIN-JetsonNano-public/blob/main/fan/config.json). For further information, visit [jetson fan repository](<https://github.com/Pyrestone/jetson-fan-ctl.git>). Default configuration:

    ```json
    {
    "FAN_OFF_TEMP":20,
    "FAN_MAX_TEMP":45,
    "UPDATE_INTERVAL":5,
    "MAX_PERF":1
    }
    ```

5. **Swapfile Configuration (Optional)**  
    To configure the swapfile, edit this line below in [``init.sh``](https://github.com/OPIN-Smart-Home/OPIN-JetsonNano-public/blob/main/init.sh). Default configuration is 12 GB.
    ```bash
    ./installSwapfile.sh -s 12
    ```

6. **Install Dependencies**
    ```bash
    cd
    cd OPIN-JetsonNano-public/
    sudo ./init.sh
    ```
    >**Note**: The system will reboot after installation


## Device Manager System (Node-RED)
The Device Manager System in the OPIN Smart Home leverages Node-RED to facilitate the management and control of various smart devices within your home. This section outlines the setup process for Node-RED using Docker, enabling easy deployment and management of smart devices.
### Setup
1. **Ensure Docker Service is Enabled**  
    To check if Docker is enabled to start on boot (look for ``enabled`` in the output), run:
    ```bash
    sudo systemctl status docker
    ```
    If the output ``disabled``, enable it with running this:
    ```bash
    sudo systemctl enable docker
    ```

2. **Build OPIN Docker Image**  
    Navigate to the directory containing Dockerfile, [``/nodeRED/Dockerfile``](https://github.com/OPIN-Smart-Home/OPIN-JetsonNano-public/blob/main/nodeRED/Dockerfile), and run:
    ```bash
    cd
    cd OPIN-JetsonNano-public/nodeRED/
    sudo docker build --network=host -t opin:latest .
    ```
    - ``docker build``  
    This is the Docker command used to build a Docker image from a Dockerfile. It reads the Dockerfile and the context (files and directories in the specified path) to create an image.
    - ``--network=host``  
    This option tells Docker to use the host's networking stack for the build process. It allows the build to access network resources on the host directly, which can be useful for downloading dependencies or communicating with services during the image build.
    - ``-t opin:latest``  
    This flag is used to tag the image being built. ``opin`` is the name of the image. ``latest`` is the tag for the image version. This conventionally indicates that this is the most recent version of the image. Tags help manage different versions of an image.
    - ``.``  
    This dot signifies the build context, which is the current directory. Docker will look for a Dockerfile and any files in this directory to include in the build process.

3. **Create OPIN Container**  
    Execute the container with the following command, ensure to map the appropriate ports and volumes:
    ```bash
    sudo docker run -d --restart=always --name opin -p 1880:1880 -p 5432:5432 -v /var/run/docker.sock:/var/run/docker.sock opin:latest
    ```
    - ``docker run``  
    Docker command to run/create a container from an image. 
    - ``-d``  
    Detached mode, run the container in the background, allowing terminal to be freed up for other tasks.
    - ``--restart=always``  
    Ensures that the container will always restart automatically if it stops, crashes, or the Docker daemon restarts a.k.a automatically start the container when the system boots up. It is useful for keeping services running long-term.
    - ``--name opin``  
    This specifies the name of the container as opin, can easily refer to it later (e.g., when using docker exec, docker stop, etc.).
    - ``-p 1880:1880``  
    This maps port 1880 on host machine to port 1880 inside the container. Port 1880 is used for Node-RED, so this makes the Node-RED service running inside the container accessible from your host.
    - ``-p 5432:5432``  
    This maps port 5432 on host machine to port 5432 inside the container. Port 5432 is the default port for PostgreSQL, so this makes the PostgreSQL database service running inside the container accessible from your host.
    - ``-v /var/run/docker.sock:/var/run/docker.sock``  
    This mounts the Docker socket file (/var/run/docker.sock) from the host into the container, allowing the container to communicate with the Docker daemon on the host. It enables the opin container to run Docker commands and manage other containers from within itself ([auto-off container](#auto-off-system-setup-human-detection)). 
    - ``opin:latest``  
    This is the image name (opin) and the tag (latest). It tells Docker to use the latest version of the opin image to create the container. If no tag is specified, Docker defaults to latest.

### Additional
1. **Access Node-RED Editor**  
    To access the Node-RED editor, open web browser and navigate to: ``http://localhost:1880``.

2. **Environment Variables for PostgreSQL**  
    ```Dockerfile
    ENV POSTGRES_USER=opin
    ENV POSTGRES_PASSWORD=postgresql
    ENV POSTGRES_DB=opin
    ```

3. **Gateway / Jetson Nano UID**  
    The UID consists of 16 random characters. This UID is used to identify the gateway and serves as authentication for users attempting to connect to the gateway for the first time. The UID is generated, hard-coded, and stored in [``/nodeRED/uid.txt``](https://github.com/OPIN-Smart-Home/OPIN-JetsonNano-public/blob/main/nodeRED/uid.txt) and [``/autoOffCam/uid.txt``](https://github.com/OPIN-Smart-Home/OPIN-JetsonNano-public/blob/main/autoOffCam/uid.txt).

4. **Firebase Realtime Database**  
    To access the firebase, feel free to contact [me](#further-information).


## Auto-Off System (Human Detection)
The Auto-Off System leverages human detection technology to enhance energy efficiency and safety in the OPIN Smart Home system. This section provides a step-by-step guide for setting up the auto-off functionality based on human presence detection using Docker.
### Setup
1. **Build Auto-Off Docker Image**  
    Navigate to the directory containing Dockerfile, [``/autoOffCam/Dockerfile``](https://github.com/OPIN-Smart-Home/OPIN-JetsonNano-public/blob/main/autoOffCam/Dockerfile), and run:
    ```bash
    cd
    cd OPIN-JetsonNano-public/autoOffCam/
    sudo docker build --network=host -t auto-off-cam:latest .
    ```
    - ``docker build``  
    This is the Docker command used to build a Docker image from a Dockerfile. It reads the Dockerfile and the context (files and directories in the specified path) to create an image.
    - ``--network=host``  
    This option tells Docker to use the host's networking stack for the build process. It allows the build to access network resources on the host directly, which can be useful for downloading dependencies or communicating with services during the image build.
    - ``-t auto-off-cam:latest``  
    This flag is used to tag the image being built. ``auto-off-cam`` is the name of the image. ``latest`` is the tag for the image version. This conventionally indicates that this is the most recent version of the image. Tags help manage different versions of an image.
    - ``.``  
    This dot signifies the build context, which is the current directory. Docker will look for a Dockerfile and any files in this directory to include in the build process.
    >**Note**: No need to create container. It will be created once IP Camrera is added by user using mobile application. If you want to experiment, you can create the container by following the next step

2. **Create Auto-Off Container**  
    Execute the container with the following command, ensure to map the appropriate ports and volumes:
    ```bash
    sudo docker run --name ip_camera --ipc=host --runtime=nvidia --gpus all auto-off-cam:latest
    ```
    - ``docker run``  
    Docker command to run/create a container from an image.
    - ``--name ip_camera``  
    This specifies the name of the container as ip_camera, can easily refer to it later (e.g., when using docker exec, docker stop, etc.).
    - ``--ipc=host``  
    This option sets the IPC (Inter-Process Communication) mode for the container to use the host's IPC namespace. This allows processes in the container to communicate with processes on the host machine, which can be useful for sharing memory or other IPC mechanisms.
    - ``--runtime=nvidia``  
    This flag specifies that the container should use the NVIDIA runtime for Docker. This is necessary for running containers that utilize NVIDIA GPUs, allowing them to access GPU resources. 
    - ``--gpus all``  
    This argument requests access to all available GPUs on the host for the container. This enables GPU acceleration within the container for applications that require it (such as machine learning, video processing, etc.).
    - ``auto-off-cam:latest``  
    This is the image name (auto-off-cam) and the tag (latest). It tells Docker to use the latest version of the opin image to create the container. If no tag is specified, Docker defaults to latest.

### Additional
1. **Monitor Gateway Resources**  
    Resources of the Jetson Nano gateway can be monitored using `jtop`, which is especially useful for tracking GPU usage. Run `jtop` to start monitoring:
     ```bash
     jtop
     ```

2. **Experimental Files**  
   These files are located in [``etc``](https://github.com/OPIN-Smart-Home/OPIN-JetsonNano-public/tree/main/etc) directory and consist of previous trials and errors that might still be useful for future development.


3. **Gateway / Jetson Nano UID**  
    The UID consists of 16 random characters. This UID is used to identify the gateway and serves as authentication for users attempting to connect to the gateway for the first time. The UID is generated, hard-coded, and stored in [``/nodeRED/uid.txt``](https://github.com/OPIN-Smart-Home/OPIN-JetsonNano-public/blob/main/nodeRED/uid.txt) and [``/autoOffCam/uid.txt``](https://github.com/OPIN-Smart-Home/OPIN-JetsonNano-public/blob/main/autoOffCam/uid.txt).

4. **Firebase Realtime Database**  
    To access the firebase, feel free to contact [me](#further-information).


## Limitations
- **No Dashboard**: There is currently no web dashboard accessible via the Jetson IP.
- **Data Transfer**: TLS is not implemented for secure data transfer between the Jetson Nano and connected devices.
- **Initial Setup**: The Jetson Nano must be connected to a display, mouse, and keyboard for the first-time gateway setup.
- **IP Camera Limitation**: The system is limited to only one IP camera for the auto-off functionality.
- **AC Control Device**: The control of AC devices is limited to Panasonic. ~~Users~~ Developers must manually add IR data to the PostgreSQL database.


## Future Development
- **Web Dashboard**: Develop a web dashboard that can be accessed via the Jetson IP or public domain, providing users with a user-friendly interface to monitor and control their smart home devices.
- **Secure Data Transfer**: Implement TLS for secure communication between the Jetson Nano and connected devices to enhance security and data integrity.
- **Initial Setup Flexibility**: Explore options for a simplified setup process that may not require a display, mouse, and keyboard for the initial gateway configuration.
- **Multiple IP Camera Support**: Enhance the system to allow multiple IP cameras to be connected for auto-off functionality, enabling greater flexibility and coverage in monitoring. Another option is to upgrade the gateway to **Nvidia Jetson Orin Nano** or higher for improved performance and capabilities 👍👍
- **Optimized Swapfile Configuration**: Investigate the optimal configuration of the swapfile size and memory usage to improve performance and resource management based on real-world usage scenarios. Current swapfile size of is excessive, 12 GB; based on various experiments, 4 GB is sufficient.
- **Expanded AC Device Compatibility**: Develop an AC IR data signing device that can capture and store IR codes from various AC brands. This would allow users to control a wider range of AC units beyond just Panasonic, making the system more versatile.
- **Integration with Various Technologies**: Expand compatibility with various technologies such as Alexa, Siri, Google Assistant, and others to create a more interconnected smart home ecosystem. **Another option is to develop these technologies our own** 👍👍

---
---

# Further Information
For further information, please feel free to contact me at:
- **Email**: [anisahfarah28@gmail.com](mailto:anisahfarah28@gmail.com)
- **LinkedIn**: [Anisah Farah Fadhilah](https://www.linkedin.com/in/anisahfarahfadhilah)
