import cv2

WIDTH = 1920
HEIGHT = 1080
Y_HOR = 500
Y_HOOD = 900
X_HOOD_L = 485
X_HOOD_R = 1380
X_HOR_L = 875
X_HOR_R = 1055

def draw_line(a, b, srcpath, destpath):
  image = cv2.imread(srcpath)
  cv2.line(image, (int(a[0]),int(a[1])), (int(b[0]),int(b[1])), (255,0,0), 2)
  cv2.imwrite(destpath, image)

def get_bounding_box():
     
  top_left = (X_HOR_L, Y_HOR)
  top_right = (X_HOR_R, Y_HOR)
  bottom_left = (X_HOOD_L, Y_HOOD)
  bottom_right = (X_HOOD_R, Y_HOOD)

  return (top_left, top_right, bottom_left, bottom_right)

def main():
  img_src = "test.jpg"
  img_dest = "out.jpg"
  bb = get_bounding_box()
  #draw_line((0,0),(400,400),img_src,img_dest)
  draw_line(bb[0],bb[1],img_src,img_dest)
  draw_line(bb[0],bb[2],img_dest,img_dest)
  draw_line(bb[1],bb[3],img_dest,img_dest)
  draw_line(bb[2],bb[3],img_dest,img_dest)

if __name__ == "__main__":
  main()
