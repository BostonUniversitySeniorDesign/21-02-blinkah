# Blinah ALPR (Automated License Plate Reader)

# OpenALPR installation and setup

Set-up of OpenALPR was too difficult and outdated on windows, so installing it on an Ubuntu based system was the best option. 
Following this tutorial, https://gist.github.com/braitsch/ee5434f91744026abb6c099f98e67613, on an ubuntu, linux based OS, the steps are as follows:
* install leptonica 1.74.1 and build it
* install tesseract 3.0.5 and build it
* Check to make sure that the correct versions are installed properly
* Install libcurl3 & update libcurl4
* Download OpenALPR from github
* In build directory, setup compilation environment
* compile the library
* check with random license plate image to test functionality
