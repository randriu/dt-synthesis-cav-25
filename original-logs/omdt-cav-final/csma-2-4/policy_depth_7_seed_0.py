######################## Properties ########################
# expected discounted reward: 38.82811995685484
# expected discounted reward bound: 39.19103308390623
# value iteration: None
# proven optimal: False
# runtime: 1206.145714044571
######################## Parameters ########################
# depth: 7
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(b, y1, y2, s1, x1, bc1, cd1, s2, x2, bc2, cd2):
    if b <= 0.0:
        if cd2 <= 4.0:
            if x2 <= 26.0:
                return 'send1'
            else:
                return 'time'
        else:
            if cd2 <= 4.0:
                return 'send1'
            else:
                if cd2 <= 4.0:
                    return 'time'
                else:
                    if cd2 <= 4.0:
                        return 'send2'
                    else:
                        if cd2 <= 4.0:
                            return 'time'
                        else:
                            if cd2 <= 4.0:
                                return 'time'
                            else:
                                return 'send1'
    else:
        if cd2 <= 4.0:
            if b <= 1.0:
                return 'time'
            else:
                if y2 <= 0.0:
                    return 'cd'
                else:
                    return 'time'
        else:
            if cd2 <= 4.0:
                return 'send1'
            else:
                if cd2 <= 4.0:
                    return 'send2'
                else:
                    return 'time'
