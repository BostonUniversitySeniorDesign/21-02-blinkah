import os
import cv2
import matplotlib.pyplot as plt

def imShow(path):
    image = cv2.imread(path)
    height, width = image.shape[:2]
    resized_image = cv2.resize(image,(3*width, 3*height), interpolation = cv2.INTER_CUBIC)

    fig = plt.gcf()
    fig.set_size_inches(18, 10)
    plt.axis("off")
    plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
    plt.show()

# os.system("./setup.sh")
os.chdir("/darknet")
os.system("./darknet detect cfg/yolov3.cfg yolov3.weights -ext_output data/dog.jpg")