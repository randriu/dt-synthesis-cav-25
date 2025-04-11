######################## Properties ########################
# expected discounted reward: 0.30710759901397866
# expected discounted reward bound: 0.3487237168391304
# value iteration: None
# proven optimal: False
# runtime: 1200.0071461200714
######################## Parameters ########################
# depth: 6
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(X, Y):
    if X <= 0.0:
        if Y <= 9.0:
            if Y <= 6.0:
                if Y <= 2.0:
                    if Y <= 0.0:
                        return '(Left)'
                    else:
                        return '(Down)'
                else:
                    if Y <= 2.0:
                        return '(Down)'
                    else:
                        return '(Left)'
            else:
                if Y <= 7.0:
                    return '(Down)'
                else:
                    return '(Up)'
        else:
            if Y <= 11.0:
                return '(Down)'
            else:
                return '(Left)'
    else:
        if X <= 3.0:
            if Y <= 7.0:
                if Y <= 4.0:
                    if Y <= 3.0:
                        if X <= 2.0:
                            return '(Left)'
                        else:
                            return '(Up)'
                    else:
                        return '(Up)'
                else:
                    if X <= 1.0:
                        return '(Down)'
                    else:
                        if Y <= 6.0:
                            return '(Down)'
                        else:
                            return '(Left)'
            else:
                if Y <= 9.0:
                    if X <= 1.0:
                        if Y <= 8.0:
                            return '(Down)'
                        else:
                            return '(Right)'
                    else:
                        return '(Down)'
                else:
                    if Y <= 10.0:
                        return '(Down)'
                    else:
                        return '(Right)'
        else:
            if Y <= 4.0:
                if Y <= 2.0:
                    if X <= 5.0:
                        if X <= 4.0:
                            return '(Up)'
                        else:
                            return '(Left)'
                    else:
                        if X <= 5.0:
                            return '(Left)'
                        else:
                            return '(Up)'
                else:
                    if Y <= 3.0:
                        return '(Up)'
                    else:
                        if X <= 7.0:
                            return '(Right)'
                        else:
                            return '__random__'
            else:
                if Y <= 9.0:
                    if Y <= 8.0:
                        if Y <= 6.0:
                            return '(Up)'
                        else:
                            return '(Down)'
                    else:
                        if X <= 5.0:
                            return '(Left)'
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
