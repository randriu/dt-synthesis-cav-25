######################## Properties ########################
# expected discounted reward: 0.392685222762892
# expected discounted reward bound: 0.39269750639906736
# value iteration: None
# proven optimal: True
# runtime: 12.034327983856201
######################## Parameters ########################
# depth: 3
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(X, Y):
    if X <= 6.0:
        if X <= 5.0:
            if Y <= 0.0:
                return '(Right)'
            else:
                return '(Up)'
        else:
            if Y <= 3.0:
                return '(Right)'
            else:
                return '(Up)'
    else:
        if Y <= 0.0:
            return '(Right)'
        else:
            if Y <= 1.0:
                return '(Down)'
            else:
                return '(Right)'
