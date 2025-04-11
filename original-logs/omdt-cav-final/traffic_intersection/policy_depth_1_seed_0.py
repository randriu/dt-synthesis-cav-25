######################## Properties ########################
# expected discounted reward: -72.06683505791119
# expected discounted reward bound: -72.06683505791119
# value iteration: None
# proven optimal: True
# runtime: 13.677742958068848
######################## Parameters ########################
# depth: 1
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(green_side, cars_left, cars_right, waiting_time):
    if waiting_time <= 2.0:
        return '(wait)'
    else:
        return '(switch_light)'
