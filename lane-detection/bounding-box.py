import constant

def get_bounding_box():
    upper_y = constant.CAMERA_RES_Y * constant.HORIZON_CUTOFF_PERCENT
    lower_y = constant.CAMERA_RES_Y * constant.GROUND_CUTOFF_PERCENT

    top_left_x = constant.CAMERA_RES_X * ((1 - constant.UPPER_HORIZONTAL_SCALAR) / 2)
    top_right_x = constant.CAMERA_RES_X * (constant.UPPER_HORIZONTAL_SCALAR + (1 - constant.UPPER_HORIZONTAL_SCALAR) / 2)
    bottom_left_x = constant.CAMERA_RES_X * ((1 - constant.LOWER_HORIZONTAL_SCALAR) / 2)
    bottom_right_x = constant.CAMERA_RES_X * (constant.LOWER_HORIZONTAL_SCALAR + (1 - constant.LOWER_HORIZONTAL_SCALAR) / 2)

    top_left = (top_left_x, upper_y)
    top_right = (top_right_x, upper_y)
    bottom_left = (bottom_left_x, lower_y)
    bottom_right = (bottom_right_x, lower_y)

    return (top_left, top_right, bottom_left, bottom_right)