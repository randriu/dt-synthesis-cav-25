######################## Properties ########################
# expected discounted reward: 0.36516651443791465
# expected discounted reward bound: 0.36516651443791465
# value iteration: None
# proven optimal: True
# runtime: 0.2146470546722412
######################## Parameters ########################
# depth: 2
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(X, Y):
    if X <= 0.0:
        if Y <= 1.0:
            return '(Left)'
        else:
            return '(Up)'
    else:
        if Y <= 2.0:
            return '(Down)'
        else:
            return '(Right)'
