######################## Properties ########################
# expected discounted reward: 2.1148057199302297
# expected discounted reward bound: 2.1246055771434853
# value iteration: None
# proven optimal: False
# runtime: 1200.0024938583374
######################## Parameters ########################
# depth: 4
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(green_side, cars_left, cars_right, waiting_time):
    if green_side <= 0.0:
        if waiting_time <= 2.0:
            if cars_right <= 0.0:
                return '(wait)'
            else:
                if cars_left <= 1.0:
                    return '(switch_light)'
                else:
                    return '(wait)'
        else:
            if cars_left <= 1.0:
                if waiting_time <= 5.0:
                    return '(switch_light)'
                else:
                    return '(wait)'
            else:
                if cars_right <= 1.0:
                    return '(wait)'
                else:
                    return '(switch_light)'
    else:
        if waiting_time <= 1.0:
            if cars_left <= 1.0:
                return '(wait)'
            else:
                if cars_right <= 1.0:
                    return '(switch_light)'
                else:
                    return '(wait)'
        else:
            if cars_left <= 0.0:
                return '(wait)'
            else:
                return '(switch_light)'
