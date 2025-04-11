######################## Properties ########################
# expected discounted reward: 0.5201248227986334
# expected discounted reward bound: 0.5201248227986334
# value iteration: None
# proven optimal: True
# runtime: 0.5025279521942139
######################## Parameters ########################
# depth: 3
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
            if Y <= 3.0:
                return '(Up)'
            else:
                return '(Left)'
    else:
        if X <= 1.0:
            if Y <= 2.0:
                return '(Down)'
            else:
                return '(Right)'
        else:
            if Y <= 2.0:
                return '(Left)'
            else:
                return '(Down)'
