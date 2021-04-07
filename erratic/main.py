from jetcam.csi_camera import CSICamera
from jetcam.utils import bgr8_to_jpeg
import time
import object


def read_camera(path, camera, cnt):
  img = camera.read()
  jpg = bgr8_to_jpeg(img)
  f = open(path + "car_frame_" + str(cnt) + ".jpg", "wb")
  f.write(jpg)
  f.close()

def take_some_pictures(path):

  camera = CSICamera(width=1920, height=1080, capture_device=0)

  # Warm up the camera (Takes 12 images to warm up)
  for i in range(30):
    camera.read() 
    time.sleep(1/30)

  # Take Pictures (Max 100)
  cnt = 0
  while True:
    time.sleep(1/30)
    read_camera(path, camera,cnt)
    cnt += 1
    if cnt > 10:
      cnt = 0 
      break
      


def main():

  if False:
    img_path = "/home/blinkah/Documents/21-02-blinkah/erratic/swerving_car/car_frame_7.jpg"
    print(str(object.run_alpr(img_path)))

  if True:
    opt_input_uri = "/home/blinkah/Documents/21-02-blinkah/erratic/swerving_car/car_frame_*.jpg"
    opt_output_uri = "/home/blinkah/Documents/21-02-blinkah/erratic/analyzed/car_analy_%i.jpg" 
    opt_crop_uri = "/home/blinkah/Documents/21-02-blinkah/erratic/crop/car_frame_*.jpg"
    object.run_detect(opt_input_uri, opt_output_uri, opt_crop_uri)



  if False:
    photo_folder = "/home/blinkah/Documents/21-02-blinkah/erratic/live_photos/"
    photo_analysis = "/home/blinkah/Documents/21-02-blinkah/erratic/live_analysis/"

    ###take_some_pictures(photo_folder)

    object.run_detect(photo_folder, photo_analysis)





if __name__ == "__main__":
  main()