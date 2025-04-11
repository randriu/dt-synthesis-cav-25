######################## Properties ########################
# expected discounted reward: -0.2171856875249345
# expected discounted reward bound: -0.2171856875249345
# value iteration: None
# proven optimal: True
# runtime: 115.111074924469
######################## Parameters ########################
# depth: 2
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(green_side, cars_left, cars_right, waiting_time):
    if green_side <= 0.0:
        if cars_left <= 1.0:
            return '(switch_light)'
        else:
            return '(wait)'
    else:
        if cars_left <= 0.0:
            return '(wait)'
        else:
            return '(switch_light)'
