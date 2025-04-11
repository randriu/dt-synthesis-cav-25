######################## Properties ########################
# expected discounted reward: 0.5420259305406872
# expected discounted reward bound: 0.5420259305406872
# value iteration: None
# proven optimal: True
# runtime: 3.8669400215148926
######################## Parameters ########################
# depth: 8
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(X, Y):
    if X <= 1.0:
        if Y <= 3.0:
            if Y <= 1.0:
                if X <= 0.0:
                    return '(Left)'
                else:
                    return '(Up)'
            else:
                if Y <= 2.0:
                    if X <= 0.0:
                        if Y <= 1.0:
                            return '(Left)'
                        else:
                            return '(Up)'
                    else:
                        return '(Down)'
                else:
                    return '(Right)'
        else:
            return '(Left)'
    else:
        if Y <= 3.0:
            if Y <= 0.0:
                if X <= 2.0:
                    return '(Up)'
                else:
                    if X <= 2.0:
                        if Y <= 2.0:
                            return '__random__'
                        else:
                            return '(Left)'
                    else:
                        if Y <= 1.0:
                            return '(Up)'
                        else:
                            if X <= 2.0:
                                return '(Down)'
                            else:
                                return '__random__'
            else:
                if X <= 1.0:
                    return '__random__'
                else:
                    if Y <= 0.0:
                        return '__random__'
                    else:
                        if Y <= 0.0:
                            return '(Left)'
                        else:
                            if Y <= 2.0:
                                return '(Left)'
                            else:
                                if Y <= 2.0:
                                    return '(Left)'
                                else:
                                    return '(Down)'
        else:
            return '(Left)'
