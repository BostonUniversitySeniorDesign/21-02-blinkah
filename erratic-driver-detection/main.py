# CONSTANTS
FRAMES_TO_COOLDOWN = 120
LANE_SWITCH_THRESHOLD = 2

# Normal variables
lane_switch_counter = 0
frame_counter = 0
# 99 is an arbitrary integer used to indicate there is no active car currently detected
last_lane = 99
erraticDriverDetected = False

def erraticDriverFrameUpdate(lane_bounds, car_bounds):
    # If there is no car currently detected, run this
    if car_bounds is None:
        lane_switch_counter = 0
        frame_counter = 0
        last_lane = 99
        erraticDriverDetected = False
        return
    
    # if this is the first frame a car is being detected:
    if last_lane == 99:
        lane_switch_counter = 0
        frame_counter = 1
        last_lane = detectRelativeLane(lane_bounds, car_bounds)
    # every other time a car is detected after first:
    else:
        # get current lane we're in
        current_lane = detectRelativeLane(lane_bounds, car_bounds)

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


def detectRelativeLane(lane_bounds, car_bounds):
    car_top_y = car[0][1]
    car_bottom_y = car[2][1]
    car_left_x = car[0][0]
    car_right_x = car[1][0]

    # get the y-value a third of the way up from the bottom edge (aka two thirds of the way down from the top edge)
    car_y = ((car_bottom_y - car_top_y) * 2 // 3) + car_top_y
    # get the x-value halfway between both edges, as expected
    car_x = ((car_right_x - car_left_x) // 2) + car_left_x

    # LEFT LANE BORDER CALCULATIONS
    left_slope = 

    # RIGHT LANE BORDER CALCULATIONS


def main():
    # on every frame, call erraticDriverFrameUpdate(lane_bounds, car_bounds)
    # where lane_bounds is a tuple of 4 (x,y) coordinate points drawing a trapezoid of the lane in front of own car
    # and car_bounds is a tuple of 4 (x,y) coordinate points drawing a rectangle of the other car. Can be 'None' if no other car detected

    # IMPORTANT: the 4 coordinate pairs should be in the following order: top left, top right, bottom left, bottom right
    # and each coordinate point is a tuple of 2 integers: (x, y)

    pass

if __name__ == "__main__":
    main()