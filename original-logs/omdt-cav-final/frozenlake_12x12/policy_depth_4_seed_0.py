######################## Properties ########################
# expected discounted reward: 0.275765523265236
# expected discounted reward bound: 0.34872371683748776
# value iteration: None
# proven optimal: False
# runtime: 1200.0035259723663
######################## Parameters ########################
# depth: 4
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(X, Y):
    if Y <= 7.0:
        if X <= 2.0:
            if Y <= 6.0:
                if X <= 1.0:
                    return '(Left)'
                else:
                    return '(Down)'
            else:
                if X <= 1.0:
                    return '(Down)'
                else:
                    return '(Left)'
        else:
            if X <= 3.0:
                if Y <= 5.0:
                    return '(Down)'
                else:
                    return '(Up)'
            else:
                if X <= 4.0:
                    return '(Up)'
                else:
                    return '(Down)'
    else:
        if X <= 1.0:
            if Y <= 8.0:
                if X <= 0.0:
                    return '(Up)'
                else:
                    return '(Down)'
            else:
                if Y <= 9.0:
                    return '(Right)'
                else:
                    return '(Down)'
        else:
            if Y <= 10.0:
                return '(Down)'
            else:
                if X <= 6.0:
                    return '(Right)'
                else:
                    return '(Left)'
