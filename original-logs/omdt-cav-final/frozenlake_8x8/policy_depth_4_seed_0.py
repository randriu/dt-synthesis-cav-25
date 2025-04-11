######################## Properties ########################
# expected discounted reward: 0.4047321310334312
# expected discounted reward bound: 0.408580115627142
# value iteration: None
# proven optimal: False
# runtime: 1200.0017619132996
######################## Parameters ########################
# depth: 4
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(X, Y):
    if X <= 5.0:
        if Y <= 4.0:
            if Y <= 1.0:
                if Y <= 0.0:
                    return '(Right)'
                else:
                    return '(Up)'
            else:
                if X <= 4.0:
                    return '(Right)'
                else:
                    return '(Down)'
        else:
            if X <= 4.0:
                if X <= 3.0:
                    return '(Right)'
                else:
                    return '(Up)'
            else:
                if Y <= 5.0:
                    return '(Left)'
                else:
                    return '(Right)'
    else:
        if X <= 6.0:
            if Y <= 3.0:
                return '(Right)'
            else:
                if Y <= 5.0:
                    return '(Up)'
                else:
                    return '(Down)'
        else:
            if Y <= 2.0:
                if Y <= 0.0:
                    return '(Right)'
                else:
                    return '(Down)'
            else:
                if Y <= 2.0:
                    return '(Left)'
                else:
                    return '(Right)'
