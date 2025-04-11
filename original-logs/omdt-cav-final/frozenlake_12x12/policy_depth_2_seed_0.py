######################## Properties ########################
# expected discounted reward: 0.11767002527533808
# expected discounted reward bound: 0.11767002527533808
# value iteration: None
# proven optimal: True
# runtime: 220.99092507362366
######################## Parameters ########################
# depth: 2
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(X, Y):
    if Y <= 10.0:
        if Y <= 6.0:
            return '(Left)'
        else:
            return '(Down)'
    else:
        if X <= 6.0:
            return '(Right)'
        else:
            return '(Left)'
