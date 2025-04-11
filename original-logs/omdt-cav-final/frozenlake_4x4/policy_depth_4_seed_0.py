######################## Properties ########################
# expected discounted reward: 0.5420259305406874
# expected discounted reward bound: 0.5420259305406874
# value iteration: None
# proven optimal: True
# runtime: 0.606867790222168
######################## Parameters ########################
# depth: 4
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(X, Y):
    if X <= 1.0:
        if Y <= 2.0:
            if Y <= 1.0:
                if X <= 0.0:
                    return '(Left)'
                else:
                    return '(Up)'
            else:
                if X <= 0.0:
                    return '(Up)'
                else:
                    return '(Down)'
        else:
            if Y <= 2.0:
                return '(Left)'
            else:
                if Y <= 3.0:
                    return '(Right)'
                else:
                    return '(Left)'
    else:
        if Y <= 1.0:
            if Y <= 0.0:
                return '(Up)'
            else:
                return '(Right)'
        else:
            if X <= 1.0:
                return '(Down)'
            else:
                if Y <= 2.0:
                    return '(Left)'
                else:
                    return '(Down)'
