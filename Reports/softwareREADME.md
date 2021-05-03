# Software Report

## Machine Learning Components


### OpenALPR
21-02-blinkah/Jetson/qt5/alpr.py
OpenALPR is an open-source Automated License Plate Recognition library that we use to detect and read license plates from erratic driver images. In order to set up this tool, we had to install a lot of dependencies and test that they compiled properly. 
Using a linux OS, we had to install tesseract (for translating to text) and OpenCV. After setting the build directory, we set up the compile library and call make to test it. If it is in working order, you can test it on an image by calling alpr "image-name". 

sudo apt-get install libopencv-dev libtesseract-dev git cmake build-essential libleptonica-dev
sudo apt-get install liblog4cplus-dev libcurl3-dev
git clone https://github.com/openalpr/openalpr.git
cd openalpr/src
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr -DCMAKE_INSTALL_SYSCONFDIR:PATH=/etc ..
make
sudo make install

alpr car1.jpg

This would return a list of estimated license plates with confidence values, but we only wanted the highest confidence value estimate, so we parsed the output to return the first license plate. If alpr is unable to detect a license plate for any reason, it will output "NOIMG". For full functionality, alpr requires importing subprocess and sys. This is mainly for parsing the initial output which is given without proper formatting to the command line. The plate value and confidence interval will be output as text and returned.

## Head Unit

### QtPy5
21-02-blinkah/Jetson/qt5/ui_v3.py
The LCD UI was done using QtPy5. This was an intuitive frontend framework that allowed us to easily implement our vision for the UI. This GUI module will be used to handle the hardware functionality and look in a clean manner. The UI is broken down into buttons and images. When the ALPR button is clicked, it will run alpr which is defined as a function in the code. Likewise, the other button functionalities are for generating notifications and playing other audio clips. 

To set up QtPy5, simply run pip install PyQt5. With this, the UI designed will be run properly. 

Aside from the UI, the head unit is also in charge of the actual ML computations, so we assigned buttons with specific functionalities. We reference alpr.py for reading license plates, object.py for vehicle detection, notif_alert for generating notifications, and camera cycle to load in images in "real-time". ALPR and notif_alert are binded to buttons in order to make testing more intuitive. Once ALPR button is pressed (located to the left as a circular button), it will load an image into the frame and attempt to perform ALPR on it. Similarily, once the notification button is pressed, it will show a caution sign and play the audio until it is pressed again. 

The images used for our UI are simple logos and transparent icons, and we decided to keep it minimalistic to avoid clutter and distracting the driver. The UI also features a timer to show that it is happening in real time, and this was done via a simple date/time import. 

### Notifications
21-02-blinkah/Jetson/qt5/notif_alert.py & 21-02-blinkah/Jetson/notifications/full_notif.py
To generate notifications, we are using IBM Watson TTS to translate a text message into audio. This will be done via an API call to get the proper voice. In full_notif.py, the actual text to speech is being created after the IBM Watson TTS API call. This is saved as an mp3 file, and both the audio and text of the notification are sent to the server via POST request.

Notif_alert.py handles the actual playing of the audio on the hardware unit. Notif_alert makes a GET request to the server, specifically the url for where our notifications are being stored. Once the request is successful, it will retrieve the audio and text, and this will play the audio out loud using the speakers connected to the head unit from a system call. This file is referenced in the QT5 ui.py file to test notifications. 


## Backend 

## BCF

