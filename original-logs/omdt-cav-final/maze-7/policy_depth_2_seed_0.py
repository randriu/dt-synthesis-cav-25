######################## Properties ########################
# expected discounted reward: 2.597556995375121
# expected discounted reward bound: 5.1795799466000325
# value iteration: None
# proven optimal: False
# runtime: 1200.0065989494324
######################## Parameters ########################
# depth: 2
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(picked0, picked1, picked2, picked3, picked4, picked5, picked6, x, y):
    if x <= 5.0:
        if y <= 5.0:
            return 'u'
        else:
            return 'r'
    else:
        if x <= 7.0:
            return 'r'
        else:
            return '__random__'
