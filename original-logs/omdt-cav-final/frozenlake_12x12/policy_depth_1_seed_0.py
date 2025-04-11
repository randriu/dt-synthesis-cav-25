######################## Properties ########################
# expected discounted reward: 0.020659799611383447
# expected discounted reward bound: 0.020659799611383447
# value iteration: None
# proven optimal: True
# runtime: 2.3416550159454346
######################## Parameters ########################
# depth: 1
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(X, Y):
    if Y <= 6.0:
        return '(Left)'
    else:
        return '(Right)'
