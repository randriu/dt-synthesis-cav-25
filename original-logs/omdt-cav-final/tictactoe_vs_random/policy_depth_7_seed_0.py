######################## Properties ########################
# expected discounted reward: -0.8149295734752299
# expected discounted reward bound: 680.5705501510015
# value iteration: None
# proven optimal: False
# runtime: 1200.2246549129486
######################## Parameters ########################
# depth: 7
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(top_left_free, top_left_cross, top_left_circle, top_center_free, top_center_cross, top_center_circle, top_right_free, top_right_cross, top_right_circle, center_left_free, center_left_cross, center_left_circle, center_free, center_cross, center_circle, center_right_free, center_right_cross, center_right_circle, bottom_left_free, bottom_left_cross, bottom_left_circle, bottom_center_free, bottom_center_cross, bottom_center_circle, bottom_right_free, bottom_right_cross, bottom_right_circle):
    if bottom_right_circle <= 1.0:
        return '__random__'
    else:
        if bottom_right_circle <= 1.0:
            return '__random__'
        else:
            return '(top_left)'
