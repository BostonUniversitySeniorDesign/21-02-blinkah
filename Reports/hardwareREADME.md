# Hardware Report

### Car
This is necessary for testing purposes. Our BLINKAH unit will feature a head-unit that will typically be mounted in the car with the camera oriented properly.

### Jetson Nano 4G
This is our primary edge-computing platform. This device is responsible for running a simple UI for the LCD screen, and it is also responsible for keeping our ML computations. This device has 4 GB RAM, 16 GB storage, and runs on a Quad-core ARM Cortex-A57 MPCore Processor. Due to the limited memory and storage on the device and given the technical complexity of our project, the Jetson Nano is usually using 85%+ CPU when the UI.py file is running. 

### 7" LCD Touchscreen 1024x600
A small and simple LCD touchscreen will be used to display the basic functionalities of our dash-cam and the UI for drivers. It is connected to the Jetson Nano via HDMI, and it is mounted to the 3d Printed CAD design securely. 

### CSI-2 Camera
Our project is versatile for any camera, but for the sake of testing, we used a CSI-2 camera. This will be taking photos in real time and determining if a driver is erratic. Once the footage is deemed erratic or not, it will be sent to the server for generating reports (when required). When tested, it had proper photo quality to where license plates could be read.

### 3D Printed Hardware Mount
With a gold filament, we have a hardware mount casing for the Jetson Nano and all its connected technology. Our product should be working in cars, so this was an important step. M2 and M2.5 Stainless Steel Phillips Countersunk/Flathead screws are used to secure the LCD and Jetson Nano to the mount. THere is enough space in the casing to also hold the camera and speaker. 

### USB Speaker
A simple generic USB speaker will be used to play audio notifications. This is required mostly for showing that audio notifications are able to be generated and can alert the driver of dangerous drivers in the vicinity. 

### Hologram 4G Modem/Sim Card
This was also connected to our Jetson Nano, and this is another key piece of hardware since it allows our product to work without WIFI. This ensures that we were able to successfully test it on roads away from reliable source of WiFi. 

### Dashcam hardwire (Power)
Essentially, all the USB slots on the Jetson Nano are maxed out, and the CPU usage is also high, so our product requires a lot of power to even turn on. Initially, we tried using a powerbank, but it was not nearly enough voltage or current to power our device. As a fix, we hardwired the dashcam in our car, so it feeds the appropriate amount of power to the device.

### GT-v7 GPS Module
This requires us to be outdoors to function properly, but this will also gather accurate location data which is useful for generating incident reports.
