# BLINKAH
### Parker Van Roy, Ayush Upneja, William Pine, Ritam Das, Raghurama Bukkarayasamudram

What is “BLINKAH?” BLINKAH is a behavior-based insurance system that uses Computer Vision to analyze other drivers on the road as well as providing directions and safety notifications, as well as delivers a data analysis dashboard for enterprise insurance customers. BLINKAH Head Units are edge-computing dash cameras that leverage computer vision to analyze and report on other vehicles on the roads. Connected to the BLINKAH Computational Frontend, we analyze data from multiple head units and keep track of vehicle behavior, allowing us to create reports of erratic drivers for insurance purposes and to send warnings to drivers in the vicinity. BLINKAH ultimately eliminates irrelevant entities in traffic stops and reinforces safe driving habits.


#### Boston University Computer Engineering Senior Design Project 2020-2021

## Required Materials

1. Hardware
• Jetson Nano 4G
• CSI Camera
• 7” HDMI LCD Touchscreen
• USB Speaker
• Hologram 4G Modem & SIM
2. Head Unit Software
• OpenCV ALPR
• OpenCV MobileNet V2
• OpenCV Proprietary Lane Detection
• Erratic Driver Detection
• QtPy5 User Interface
• IBM Watson TTS & Audio Notifications
3. BCF
• Nodejs
• Django
• Firebase
• 2GB Shared Intel SSD Digital Ocean Droplet
4. Other 
• Car: 1998 Volvo V70 Cross-Country Station-wagon (AKA BLINKAH Mo- bile Transporter)

## Frontend Run Instructions

Visit https://BLINKAH.net

## Backend Run Instructions
Steps to run Django backend server in debug mode (requires Python 3, PIP, and virtualenv):

```
cd backend
source env/bin/activate
pip install -r requirements.txt
python manage.py runserver 0.0.0.0:8000
```

## Server Setup Instructions
N/A

## OpenALPR Setup Instructions
We decided to use OpenALPR, an open-source Automatic License Plate Recognition library software to handle the bulk of our computer vision and machine learning processes. It is based in C++ with dependencies available in python3, so we are using OpenCV as well as tesseract to handle the translation of license plates to text.
Since OpenALPR is based on windows and ubuntu linux, we decided to set it up on an ubuntu OS. We simply install the required prerequisites and the actual OpenALPR from the github, set up a build directory, and compile an environment. Once that is set up, we can compile the library, and install the binaries to the local machine and test. https://github.com/openalpr/openalpr/wiki/Compilation-instructions-(Ubuntu-Linux)


