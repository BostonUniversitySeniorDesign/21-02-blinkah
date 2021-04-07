import jetson.inference
import jetson.utils
from jetcam.utils import bgr8_to_jpeg

#net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.gstCamera(1920, 1080, "/dev/video0")

img = camera.capture()