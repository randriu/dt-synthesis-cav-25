######################## Properties ########################
# expected discounted reward: 0.30508202976655435
# expected discounted reward bound: 0.34872371683892944
# value iteration: None
# proven optimal: False
# runtime: 1200.0501449108124
######################## Parameters ########################
# depth: 8
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(X, Y):
    if Y <= 6.0:
        if X <= 8.0:
            if Y <= 0.0:
                if X <= 7.0:
                    if X <= 0.0:
                        return '(Left)'
                    else:
                        return '(Right)'
                else:
                    return '(Right)'
            else:
                if X <= 7.0:
                    if X <= 6.0:
                        if X <= 5.0:
                            if X <= 1.0:
                                return '(Left)'
                            else:
                                if Y <= 2.0:
                                    return '(Right)'
                                else:
                                    return '(Down)'
                        else:
                            if Y <= 5.0:
                                if Y <= 3.0:
                                    return '(Down)'
                                else:
                                    return '(Up)'
                            else:
                                return '(Down)'
                    else:
                        return '(Right)'
                else:
                    if X <= 7.0:
                        return '(Left)'
                    else:
                        if Y <= 5.0:
                            return '(Left)'
                        else:
                            return '(Down)'
        else:
            if Y <= 5.0:
                if X <= 9.0:
                    return '(Left)'
                else:
                    if Y <= 2.0:
                        return '(Left)'
                    else:
                        return '(Down)'
            else:
                return '(Down)'
    else:
        if Y <= 10.0:
            if X <= 6.0:
                if Y <= 8.0:
                    if Y <= 7.0:
                        if X <= 3.0:
                            if X <= 1.0:
                                return '(Down)'
                            else:
                                return '(Left)'
                        else:
                            if X <= 4.0:
                                return '(Right)'
                            else:
                                return '(Down)'
                    else:
                        if X <= 4.0:
                            if X <= 0.0:
                                return '(Up)'
                            else:
                                return '(Down)'
                        else:
                            if X <= 5.0:
                                return '(Up)'
                            else:
                                return '(Down)'
                else:
                    if Y <= 9.0:
                        if X <= 3.0:
                            if X <= 1.0:
                                return '(Right)'
                            else:
                                return '(Down)'
                        else:
                            if X <= 4.0:
                                return '(Left)'
                            else:
                                return '(Right)'
                    else:
                        return '(Down)'
            else:
                if X <= 9.0:
                    if Y <= 8.0:
                        if X <= 7.0:
                            if Y <= 7.0:
                                return '(Down)'
                            else:
                                return '(Left)'
                        else:
                            if Y <= 7.0:
                                if X <= 8.0:
                                    return '(Up)'
                                else:
                                    return '(Down)'
                            else:
                                if X <= 8.0:
                                    return '(Left)'
                                else:
                                    return '(Right)'
                    else:
                        if X <= 8.0:
                            return '(Down)'
                        else:
                            if Y <= 9.0:
                                return '(Left)'
                            else:
                                return '(Down)'
                else:
                    if Y <= 8.0:
                        if Y <= 7.0:
                            return '(Down)'
                        else:
                            return '(Up)'
                    else:
                        if Y <= 8.0:
                            return '(Left)'
                        else:
                            return '(Down)'
        else:
            if X <= 6.0:
                if Y <= 9.0:
                    if X <= 6.0:
                        return '(Right)'
                    else:
                        return '(Left)'
                else:
                    if Y <= 11.0:
                        if X <= 0.0:
                            return '(Down)'
                        else:
                            return '(Right)'
                    else:
                        return '(Left)'
            else:
                if X <= 10.0:
                    return '(Left)'
                else:
                    if X <= 10.0:
                        return '(Left)'
                    else:
                        if X <= 10.0:
                            return '(Left)'
                        else:
                            if X <= 10.0:
                                return '(Left)'
                            else:
                                if X <= 10.0:
                                    return '(Left)'
                                else:
                                    return '(Down)'
