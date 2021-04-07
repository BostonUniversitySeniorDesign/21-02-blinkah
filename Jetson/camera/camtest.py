from jetcam.csi_camera import CSICamera
from jetcam.utils import bgr8_to_jpeg
import time


camera = CSICamera(width=1920, height=1080, capture_device=0)

def read_camera(camera, cnt):
  img = camera.read()
  jpg = bgr8_to_jpeg(img)
  f = open("images/cap" + str(cnt) + ".jpg", "wb")
  f.write(jpg)
  f.close()

# Warm up the camera (Takes 12 images to warm up)
for i in range(30):
  camera.read() 
  time.sleep(1/30)

# Take Pictures (Max 100)
cnt = 0
while True:
  time.sleep(1/30)
  read_camera(camera,cnt)
  cnt += 1
  if cnt > 99:
    cnt = 0

