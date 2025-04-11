######################## Properties ########################
# expected discounted reward: 955.3471856645263
# expected discounted reward bound: 955.3471856645263
# value iteration: None
# proven optimal: True
# runtime: 139.5393409729004
######################## Parameters ########################
# depth: 1
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(inventory):
    if inventory <= 1.0:
        return '(Buy_12)'
    else:
        return '(Buy_8)'
