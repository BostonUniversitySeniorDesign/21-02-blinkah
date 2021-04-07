from jetcam.csi_camera import CSICamera
from jetcam.utils import bgr8_to_jpeg
import time

import multiprocessing
from multiprocessing import Process, Queue
import object

SECONDS_LOGGED = 30
FPS = 1

def read_camera(path, camera, cnt):
  #print("Tryna Read")
  img = camera.read()
  jpg = bgr8_to_jpeg(img)
  f = open(path.replace("*", str(cnt)), "wb")
  f.write(jpg)
  f.close()

def take_pictures(path, camera):
  global FPS
  global SECONDS_LOGGED
  
  # Warm up the camera (Takes 12 images to warm up)
  for i in range(30):
    camera.read() 
    time.sleep(1/30)

  # Take Pictures (Max 100)
  cnt = 0
  while True:
    time.sleep(1/FPS)
    read_camera(path, camera, cnt)
    cnt += 1
    if cnt > (SECONDS_LOGGED*FPS):
      cnt = 0 
      break
      


def pseudo_cameracycle(cc_q):
  
  pseudo_raw_img_1 = "/home/blinkah/Documents/21-02-blinkah/captures/pseudo_raw1/frame_*.jpg"
  pseudo_anal_img_1 = "/home/blinkah/Documents/21-02-blinkah/captures/pseudo_anal1/frame_%i.jpg"
  pseudo_crop_img_1 = "/home/blinkah/Documents/21-02-blinkah/captures/pseudo_crop1/frame_*.jpg"

  pseudo_raw_img_2 = "/home/blinkah/Documents/21-02-blinkah/captures/pseudo_raw2/frame_*.jpg"
  pseudo_anal_img_2 = "/home/blinkah/Documents/21-02-blinkah/captures/pseudo_anal2/frame_%i.jpg"
  pseudo_crop_img_2 = "/home/blinkah/Documents/21-02-blinkah/captures/pseudo_crop2/frame_*.jpg"

  #master_list = []
  
  while True:
    #master_list = []
    #out_q = Queue()
    net = Process(target = object.run_detect, args=(pseudo_raw_img_1, pseudo_anal_img_1, pseudo_crop_img_1, cc_q))
    net.start()
    net.join()
    if cc_q.qsize() != 0:
      break
    #if len(master_list):
    #  print(master_list)
    #  break


    #out_q = Queue()
    #master_list = []
    net = Process(target = object.run_detect, args=(pseudo_raw_img_2, pseudo_anal_img_2, pseudo_crop_img_2, cc_q))
    net.start()
    net.join()
    if cc_q.qsize() != 0:
      break
    #if len(master_list):
    #  print(master_list)
    #  break
  
  #for elem in master_list:
  #  cc_q.append(elem)
    
'''
def cameracycle(cc_q):
  
  raw_img_1 = "/home/blinkah/Documents/21-02-blinkah/captures/raw1/frame_*.jpg"
  anal_img_1 = "/home/blinkah/Documents/21-02-blinkah/captures/anal1/frame_%i.jpg"
  crop_img_1 = "/home/blinkah/Documents/21-02-blinkah/captures/crop1/frame_*.jpg"

  raw_img_2 = "/home/blinkah/Documents/21-02-blinkah/captures/raw2/frame_*.jpg"
  anal_img_2 = "/home/blinkah/Documents/21-02-blinkah/captures/anal2/frame_%i.jpg"
  crop_img_2 = "/home/blinkah/Documents/21-02-blinkah/captures/crop2/frame_*.jpg"

  pics = Process(target = take_pictures, args=(raw_img_1,))
  pics.start()
  pics.join()
'''
  # while True:

  #   net = Process(target = object.run_detect, args=(raw_img_1, anal_img_1, crop_img_1, cc_q))
  #   pics = Process(target = take_pictures, args=(raw_img_2,))
  #   net.start()
  #   pics.start()
  #   net.join()
  #   pics.join()
  #   if cc_q.qsize() != 0:
  #     break

  #   net = Process(target = object.run_detect, args=(raw_img_2, anal_img_2, crop_img_2, cc_q))
  #   pics = Process(target = take_pictures, args=(raw_img_1,))
  #   net.start()
  #   pics.start()
  #   net.join()
  #   pics.join()
  #   if cc_q.qsize() != 0:
  #     break

    
def cameracycle(cc_q):
  raw_img_1 = "/home/blinkah/Documents/21-02-blinkah/captures/raw1/frame_*.jpg"
  anal_img_1 = "/home/blinkah/Documents/21-02-blinkah/captures/anal1/frame_%i.jpg"
  crop_img_1 = "/home/blinkah/Documents/21-02-blinkah/captures/crop1/frame_*.jpg"

  raw_img_2 = "/home/blinkah/Documents/21-02-blinkah/captures/raw2/frame_*.jpg"
  anal_img_2 = "/home/blinkah/Documents/21-02-blinkah/captures/anal2/frame_%i.jpg"
  crop_img_2 = "/home/blinkah/Documents/21-02-blinkah/captures/crop2/frame_*.jpg"

  camera = CSICamera(width=1920, height=1080, capture_device=0)

  print("STARTING 1")
  t1 = time.time()
  print(str(t1))

  take_pictures(raw_img_1, camera)

  #pics = Process(target = take_pictures, args=(raw_img_1,))
  #pics.start()
  #pics.join()

  while True:
    
    t2 = time.time()-t1
    t_tot = time.time()-t1

    print("STARTING 2")
    print("Component Time: " + str(t2))
    print("Total Time: " + str(t_tot))

    net = Process(target = object.run_detect, args=(raw_img_1, anal_img_1, crop_img_1,cc_q,))
    #pics = Process(target = take_pictures, args=(raw_img_2,camera,))
    take_pictures(raw_img_2, camera)
    net.start()
    #pics.start()

    net.join()
    #pics.join()
    if cc_q.qsize() != 0:
      break

    t3 = time.time()-t2
    t_tot = time.time()-t1
    print("STARTING 3")
    print("Component Time: " + str(t3))
    print("Total Time: " + str(t_tot))

    net = Process(target = object.run_detect, args=(raw_img_2, anal_img_2, crop_img_2,cc_q,))
    #pics = Process(target = take_pictures, args=(raw_img_1,camera,))
    take_pictures(raw_img_1, camera)
    
    net.start()
    #pics.start()
    net.join()
    #pics.join()
    if cc_q.qsize() != 0:
      break

    t4 = time.time()-t3
    t_tot = time.time()-t1
    print("Component Time: " + str(t4))
    print("Total Time: " + str(t_tot))


'''
def cameracycle():

  raw_img_1 = "/home/blinkah/Documents/21-02-blinkah/captures/raw1/frame_*.jpg"
  anal_img_1 = "/home/blinkah/Documents/21-02-blinkah/captures/anal1/frame_%i.jpg"
  crop_img_1 = "/home/blinkah/Documents/21-02-blinkah/captures/crop1/frame_*.jpg"

  raw_img_2 = "/home/blinkah/Documents/21-02-blinkah/captures/raw2/frame_*.jpg"
  anal_img_2 = "/home/blinkah/Documents/21-02-blinkah/captures/anal2/frame_%i.jpg"
  crop_img_2 = "/home/blinkah/Documents/21-02-blinkah/captures/crop2/frame_*.jpg"

  print("STARTING 1")
  t1 = time.time()
  print(str(t1))

  pics = Process(target = take_pictures, args=(raw_img_1,))
  pics.start()
  pics.join()

  breaker = multiprocessing.Value("i", 0, lock=False)

  while True:
    
    t2 = time.time()-t1
    t_tot = time.time()-t1

    print("STARTING 2")
    print("Component Time: " + str(t2))
    print("Total Time: " + str(t_tot))    

    net = Process(target = object.run_detect, args=(raw_img_1, anal_img_1, crop_img_1, breaker))
    pics = Process(target = take_pictures, args=(raw_img_2,))
    net.start()
    pics.start()

    net.join()
    pics.join()

    if breaker.value == 1:
      break


    t3 = time.time()-t2
    t_tot = time.time()-t1
    print("STARTING 3")
    print("Component Time: " + str(t3))
    print("Total Time: " + str(t_tot))

    net = Process(target = object.run_detect, args=(raw_img_2, anal_img_2, crop_img_2, breaker))
    pics = Process(target = take_pictures, args=(raw_img_1,))
    
    net.start()
    pics.start()
    net.join()
    pics.join()

    t4 = time.time()-t3
    t_tot = time.time()-t1
    print("Component Time: " + str(t4))
    print("Total Time: " + str(t_tot))

    if breaker.value == 1:
      break



  # if False:
  #   img_path = "/home/blinkah/Documents/21-02-blinkah/erratic/swerving_car/frame_7.jpg"
  #   print(str(object.run_alpr(img_path)))

  # if False:
  #   opt_input_uri = "/home/blinkah/Documents/21-02-blinkah/erratic/swerving_car/frame_*.jpg"
  #   opt_output_uri = "/home/blinkah/Documents/21-02-blinkah/erratic/analyzed/analy_%i.jpg" 
  #   opt_crop_uri = "/home/blinkah/Documents/21-02-blinkah/erratic/crop/frame_*.jpg"
  #   object.run_detect(opt_input_uri, opt_output_uri, opt_crop_uri)

  # if False:
  #   photo_folder = "/home/blinkah/Documents/21-02-blinkah/erratic/live_photos/"
  #   photo_analysis = "/home/blinkah/Documents/21-02-blinkah/erratic/live_analysis/"

  #   ###take_some_pictures(photo_folder)
  #   object.run_detect(photo_folder, photo_analysis)
'''






  # if False:
  #   img_path = "/home/blinkah/Documents/21-02-blinkah/erratic/swerving_car/frame_7.jpg"
  #   print(str(object.run_alpr(img_path)))

  # if False:
  #   opt_input_uri = "/home/blinkah/Documents/21-02-blinkah/erratic/swerving_car/frame_*.jpg"
  #   opt_output_uri = "/home/blinkah/Documents/21-02-blinkah/erratic/analyzed/analy_%i.jpg" 
  #   opt_crop_uri = "/home/blinkah/Documents/21-02-blinkah/erratic/crop/frame_*.jpg"
  #   object.run_detect(opt_input_uri, opt_output_uri, opt_crop_uri)

  # if False:
  #   photo_folder = "/home/blinkah/Documents/21-02-blinkah/erratic/live_photos/"
  #   photo_analysis = "/home/blinkah/Documents/21-02-blinkah/erratic/live_analysis/"

  #   ###take_some_pictures(photo_folder)
  #   object.run_detect(photo_folder, photo_analysis)

def main():
  cc_q = Queue()
  cameracycle(cc_q)
  return cc_q

if __name__ == '__main__':
  main()