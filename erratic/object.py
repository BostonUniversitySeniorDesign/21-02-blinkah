import jetson.inference
import jetson.utils
from PIL import Image


import sys
import time
import json


import alpr
import bounding_box as bb
import swerve
import reporter

def handle_erratic(opt_input_uri, opt_crop_uri, cnt, detected_car):
  img_path = opt_input_uri.replace("*", str(cnt))
  crop_path = opt_crop_uri.replace("*", str(cnt))
  crop_img(img_path, crop_path, detected_car)
  plate, conf = run_alpr(crop_path)
  swerve.reset()
  reporter.report(img_path, 69, plate, conf)
  

def run_alpr(path):
  plates = alpr.alpr(path)
  plate = plates[0].get('license_plate')
  conf = plates[0].get('confidence')

  return plate, conf

def crop_img(path, crop_path, detected_car):
  im = Image.open(path)
  im_crop = im.crop((detected_car['left'], detected_car['top'], detected_car['right'], detected_car['bottom']))
  im_crop.save(crop_path)

def run_detect(opt_input_uri, opt_output_uri, opt_crop_uri):
    
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
    #if len(detections) == 0:
      #f.write("No Vehicle Detected\n")
    

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
    
    #f.write(str(get_car_pos(detected_cars[0])))

    # render the image
    output_uri.Render(img)

    # update the title bar
    output_uri.SetStatus("{:s} | Network {:.0f} FPS".format(opt_network, net.GetNetworkFPS()))

    # print out performance info
    #net.PrintProfilerTimes()
    if len(detected_cars):
      swerve.erraticDriverFrameUpdate(bb.get_bounding_box(), detected_cars[0])
      f.write(str(swerve.last_lane))
      f.write(str(swerve.erraticDriverDetected))
      if swerve.erraticDriverDetected:
        handle_erratic(opt_input_uri, opt_crop_uri, cnt, detected_cars[0])




    cnt +=1

    # exit on input/output EOS
    if not input_uri.IsStreaming() or not output_uri.IsStreaming():
      break

  f.close()


  



def get_car_pos(detected_car):
  return ((detected_car['left'] + detected_car['right'])/ 2,detected_car['bottom'])







