import jetson.inference
import jetson.utils
#from jetcam.csi_camera import CSICamera

import sys
import time
import json




def run_detect(opt_input_uri, opt_output_uri):
    
  opt_network = "ssd-mobilenet-v2"
  opt_overlay = "box,labels,conf"
  opt_threshold = 0.5

  is_headless = ["--headless"]

  # load the object detection network
  net = jetson.inference.detectNet(opt_network, sys.argv, opt_threshold)

  # create video sources & outputs
  input_uri = jetson.utils.videoSource(opt_input_uri, argv=sys.argv)
  output_uri = jetson.utils.videoOutput(opt_output_uri, argv=sys.argv+is_headless)


  f = open("console.txt", "w")

  cnt = 0

  # process frames until the user exits
  while True:

    # capture the next image
    img = input_uri.Capture()

    # detect objects in the image (with overlay)
    detections = net.Detect(img, overlay=opt_overlay)

    img_break = "\nImage " + str(cnt) + "\n"
    f.write(img_break)
    if len(detections) == 0:
      f.write("No Vehicle Detected\n")
    

    detected_cars = []

    detection_car_cnt = 0
    for i in range(len(detections)):
      if detections[i].ClassID == 3:
        
        detected_car = {
          'id': detection_car_cnt,
          'conf': detections[i].Confidence,
          'left': detections[i].Left,
          'right': detections[i].Right,
          'top': detections[i].Top,
          'bottom': detections[i].Bottom,
          }

        detected_cars.append(detected_car)

        #object_break = str(detection_car_cnt) + ". Conf:" + str(detections[i].Confidence) + " | bounds (tblr):  " + str(detections[i].Top) + ", " + str(detections[i].Bottom) + ", " + str(detections[i].Left) + ", " + str(detections[i].Right) + "\n"
        #f.write(object_break)
        detection_car_cnt+=1
    
    f.write(str(get_car_pos(detected_cars[0])))


    # for i in range(len(detections)):
    #   # filter for cars only
    #   if detections[i].ClassID == 3:
    #     object_break = "Car " + str(i) +" | conf:" + str(detections[i].Confidence) + " | area: " + str(detections[i].Area) + " | center: " + str(detections[i].Center) + "\n"
    #     f.write(object_break)
    #     #f.write("\tClassID: " + str(detections[i].ClassID) + "\n")


    # render the image
    output_uri.Render(img)

    # update the title bar
    output_uri.SetStatus("{:s} | Network {:.0f} FPS".format(opt_network, net.GetNetworkFPS()))

    # print out performance info
    #net.PrintProfilerTimes()
    
    cnt +=1

    # exit on input/output EOS
    if not input_uri.IsStreaming() or not output_uri.IsStreaming():
      break


  f.close()

def get_car_pos(detected_car):
  return ((detected_car['left'] + detected_car['right'])/ 2,detected_car['bottom'])
  




# def read_camera(camera, cnt):
#   img = camera.read()
#   jpg = bgr8_to_jpeg(img)
#   f = open("images/cap" + str(cnt) + ".jpg", "wb")
#   f.write(jpg)
#   f.close()




def main():

  opt_input_uri = "/home/blinkah/Documents/21-02-blinkah/erratic/swerving_car/car_frame_*.jpg"
  opt_output_uri = "/home/blinkah/Documents/21-02-blinkah/erratic/analyzed/car_analy_%i.jpg" 
  run_detect(opt_input_uri, opt_output_uri)

  #f = open("analysis.txt", "w")

  #f.write(str(get_car_pos)

  #f.close()

  # camera = CSICamera(width=1920, height=1080, capture_device=0)
  
  # Warm up the camera (Takes >12 images to warm up)
  # for i in range(30):
  #  camera.read() 
  #  time.sleep(1/30)

  # Take Pictures (Max 100)
  # cnt = 0
  # while True:
  #   time.sleep(1)
  #   read_camera(camera,cnt)
  #   detect_obj("images/cap" + str(cnt) + ".jpg", "images/det" + str(cnt) + ".jpg")
  #   cnt += 1
  #   if cnt > 10:
  #     cnt = 0

  #detect_obj("sample_data/car11")
  #camera = jetson.utils.videoSource("/dev/video0")



if __name__ == "__main__":
  main()