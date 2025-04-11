######################## Properties ########################
# expected discounted reward: 0.5420259305406874
# expected discounted reward bound: 0.5420259305406874
# value iteration: None
# proven optimal: True
# runtime: 1.4318580627441406
######################## Parameters ########################
# depth: 6
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(X, Y):
    if X <= 2.0:
        if Y <= 2.0:
            if X <= 1.0:
                if X <= 0.0:
                    if Y <= 1.0:
                        return '(Left)'
                    else:
                        return '(Up)'
                else:
                    if Y <= 0.0:
                        return '(Up)'
                    else:
                        return '(Down)'
            else:
                if Y <= 1.0:
                    if Y <= 0.0:
                        return '(Up)'
                    else:
                        return '(Right)'
                else:
                    return '(Left)'
        else:
            if Y <= 3.0:
                if X <= 0.0:
                    if Y <= 2.0:
                        return '(Up)'
                    else:
                        if Y <= 2.0:
                            return '(Left)'
                        else:
                            return '__random__'
                else:
                    if X <= 1.0:
                        return '(Right)'
                    else:
                        return '(Down)'
            else:
                return '(Left)'
    else:
        if Y <= 3.0:
            if Y <= 2.0:
                return '(Up)'
            else:
                return '__random__'
        else:
            return '(Left)'
