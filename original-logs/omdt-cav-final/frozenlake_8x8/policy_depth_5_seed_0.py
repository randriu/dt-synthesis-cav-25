######################## Properties ########################
# expected discounted reward: 0.4145189149445847
# expected discounted reward bound: 0.41464035911623487
# value iteration: None
# proven optimal: False
# runtime: 1200.0029380321503
######################## Parameters ########################
# depth: 5
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(X, Y):
    if X <= 4.0:
        if Y <= 3.0:
            if Y <= 1.0:
                if Y <= 0.0:
                    if X <= 0.0:
                        return '(Up)'
                    else:
                        return '(Right)'
                else:
                    return '(Up)'
            else:
                if X <= 3.0:
                    if Y <= 2.0:
                        return '(Left)'
                    else:
                        return '(Up)'
                else:
                    if Y <= 2.0:
                        return '(Right)'
                    else:
                        return '(Left)'
        else:
            if X <= 2.0:
                if X <= 1.0:
                    if X <= 0.0:
                        return '(Left)'
                    else:
                        return '(Down)'
                else:
                    if Y <= 6.0:
                        return '(Right)'
                    else:
                        return '(Left)'
            else:
                if X <= 3.0:
                    if Y <= 5.0:
                        return '(Right)'
                    else:
                        return '(Left)'
                else:
                    if Y <= 4.0:
                        return '(Right)'
                    else:
                        return '(Up)'
    else:
        if X <= 5.0:
            if Y <= 3.0:
                if Y <= 2.0:
                    if Y <= 1.0:
                        return '(Right)'
                    else:
                        return '(Up)'
                else:
                    if Y <= 2.0:
                        return '(Left)'
                    else:
                        return '(Down)'
            else:
                if Y <= 4.0:
                    if X <= 4.0:
                        return '(Right)'
                    else:
                        return '(Down)'
                else:
                    if Y <= 5.0:
                        return '(Left)'
                    else:
                        return '(Right)'
        else:
            if X <= 6.0:
                if Y <= 5.0:
                    if Y <= 3.0:
                        return '(Right)'
                    else:
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
                    return '(Right)'
