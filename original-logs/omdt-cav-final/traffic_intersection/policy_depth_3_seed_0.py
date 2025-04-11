######################## Properties ########################
# expected discounted reward: 1.0053302792586436
# expected discounted reward bound: 2.1246016873858924
# value iteration: None
# proven optimal: False
# runtime: 1200.003340959549
######################## Parameters ########################
# depth: 3
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(green_side, cars_left, cars_right, waiting_time):
    if cars_right <= 0.0:
        if cars_left <= 0.0:
            if green_side <= 0.0:
                return '__random__'
            else:
                return '(wait)'
        else:
            if green_side <= 0.0:
                return '(wait)'
            else:
                return '(switch_light)'
    else:
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
