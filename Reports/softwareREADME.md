# Software Report

## Machine Learning Components


## OpenALPR

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

This would return a list of estimated license plates with confidence values, but we only wanted the highest confidence value estimate, so we parsed the output to return the first license plate.
