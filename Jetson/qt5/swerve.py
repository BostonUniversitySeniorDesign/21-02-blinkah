# CONSTANTS
# ---------
FRAMES_TO_COOLDOWN = 120
LANE_SWITCH_THRESHOLD = 2

lane_switch_counter = 0
frame_counter = 0
# 99 is an arbitrary integer used to indicate there is no active car currently detected
last_lane = 99
erraticDriverDetected = False


def reset():
  global lane_switch_counter
  global frame_counter
  global last_lane
  global erraticDriverDetected

  lane_switch_counter = 0
  frame_counter = 0
  # 99 is an arbitrary integer used to indicate there is no active car currently detected
  last_lane = 99
  erraticDriverDetected = False


def erraticDriverFrameUpdate(lane_bounds, detected_car):

  global lane_switch_counter
  global frame_counter
  global last_lane
  global erraticDriverDetected

  # If there is no car currently detected, run this
  if detected_car is None:
    reset()
    return

  # if this is the first frame a car is being detected:
  if last_lane == 99:
    lane_switch_counter = 0
    frame_counter = 1
    last_lane = detectRelativeLane(lane_bounds, detected_car)
  # every other time a car is detected after first:
  else:
    # get current lane we're in
    current_lane = detectRelativeLane(lane_bounds, detected_car)

    # if we've completed one cooldown period, decrement lane switch count

    if frame_counter >= FRAMES_TO_COOLDOWN:
      if lane_switch_counter > 0:
        lane_switch_counter -= 1
      frame_counter = 0
    
    # if we've changed lanes since last frame, increment lane switch count & update last_lane
    if current_lane != last_lane:
      lane_switch_counter += 1
      last_lane = current_lane

  # Detect if we've exceeded lane switching threshold
  if lane_switch_counter > 2:
    erraticDriverDetected = True
    # TODO: Grab license plate and details of offending car, and make POST request to django backend to submit


def detectRelativeLane(lane_bounds, detected_car):
  # grab car bounds and put them in distinct variables for sanity
  car_top_y = detected_car['top']
  car_bottom_y = detected_car['bottom']
  car_left_x = detected_car['left']
  car_right_x = detected_car['right']

  # get the y-value a third of the way up from the bottom edge (aka two thirds of the way down from the top edge)
  #####car_y = ((car_bottom_y - car_top_y) * 2 // 3) + car_top_y
  car_y = car_bottom_y

  # get the x-value halfway between both edges, as expected
  car_x = ((car_right_x - car_left_x) // 2) + car_left_x

  # LEFT LANE BORDER CALCULATIONS
  # -----------------------------
  # get slope of left hand border using rise/run
  left_slope = (lane_bounds[2][1] - lane_bounds[0][1]) / (lane_bounds[2][0] - lane_bounds[0][0])
  # using point-slope, plug in `car_y` as y, and solve for x.
  # This uses the top left point, lane_bounds[0], as the point for point-slope
  left_x_bound = ((car_y - lane_bounds[0][1]) + (left_slope * lane_bounds[0][0])) / left_slope

  # RIGHT LANE BORDER CALCULATIONS
  # ------------------------------
  # get slope of right hand border using rise/run
  right_slope = (lane_bounds[3][1] - lane_bounds[1][1]) / (lane_bounds[3][0] - lane_bounds[1][0])
  # using point-slope, plug in `car_y` as y, and solve for x.
  # This uses the top right point, lane_bounds[1], as the point for point-slope
  right_x_bound = ((car_y - lane_bounds[1][1]) + (right_slope * lane_bounds[1][0])) / right_slope

  # FINAL CALCULATIONS
  # ------------------------------
  # Given the integers `left_x_bound` and `right_x_bound` which dictate the lane borders at the current y-value,
  # we will check where `car_x` is in relation to them, on a one-dimensional axis

  if car_x < left_x_bound:
    # car is to the left of the lane
    return -1
  elif car_x > right_x_bound:
    # car is to the right of the lane
    return 1
  else:
    # car is inside the lane
    return 0


# TODO!
    # on every frame, call erraticDriverFrameUpdate(lane_bounds, car_bounds)
    # where lane_bounds is a tuple of 4 (x,y) coordinate points drawing a trapezoid of the lane in front of own car
    # and car_bounds is a tuple of 4 (x,y) coordinate points drawing a rectangle of the other car. Can be 'None' if no other car detected

    # IMPORTANT: the 4 coordinate pairs should be in the following order: top left, top right, bottom left, bottom right
    # and each coordinate point is a tuple of 2 integers: (x, y)
