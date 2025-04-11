######################## Properties ########################
# expected discounted reward: 0.301020074096235
# expected discounted reward bound: 0.34872371683915127
# value iteration: None
# proven optimal: False
# runtime: 1200.0070888996124
######################## Parameters ########################
# depth: 7
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(X, Y):
    if Y <= 0.0:
        if X <= 10.0:
            if X <= 9.0:
                if X <= 4.0:
                    if X <= 2.0:
                        return '(Left)'
                    else:
                        return '(Up)'
                else:
                    if X <= 5.0:
                        return '(Up)'
                    else:
                        return '(Left)'
            else:
                return '(Left)'
        else:
            return '(Left)'
    else:
        if Y <= 0.0:
            return '(Left)'
        else:
            if Y <= 8.0:
                if X <= 4.0:
                    if Y <= 6.0:
                        if Y <= 4.0:
                            return '(Left)'
                        else:
                            if X <= 0.0:
                                return '(Left)'
                            else:
                                return '(Down)'
                    else:
                        if Y <= 7.0:
                            if X <= 1.0:
                                return '(Down)'
                            else:
                                return '(Left)'
                        else:
                            if X <= 0.0:
                                return '(Up)'
                            else:
                                return '(Down)'
                else:
                    if Y <= 4.0:
                        if Y <= 2.0:
                            return '(Up)'
                        else:
                            if X <= 10.0:
                                return '(Up)'
                            else:
                                return '(Down)'
                    else:
                        if Y <= 7.0:
                            if X <= 10.0:
                                return '(Down)'
                            else:
                                return '(Up)'
                        else:
                            if X <= 5.0:
                                return '(Up)'
                            else:
                                return '(Left)'
            else:
                if X <= 1.0:
                    if Y <= 9.0:
                        if X <= 0.0:
                            return '(Down)'
                        else:
                            return '(Right)'
                    else:
                        if X <= 0.0:
                            return '(Down)'
                        else:
                            if Y <= 10.0:
                                return '(Down)'
                            else:
                                return '(Right)'
                else:
                    if X <= 5.0:
                        if Y <= 9.0:
                            if X <= 3.0:
                                return '(Down)'
                            else:
                                return '(Left)'
                        else:
                            if Y <= 10.0:
                                return '(Down)'
                            else:
                                return '(Right)'
                    else:
                        if Y <= 10.0:
                            if X <= 6.0:
                                return '(Right)'
                            else:
                                return '(Down)'
                        else:
                            if X <= 6.0:
                                return '(Right)'
                            else:
                                return '(Left)'
