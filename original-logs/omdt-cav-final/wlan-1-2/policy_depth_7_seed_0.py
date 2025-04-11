######################## Properties ########################
# expected discounted reward: 0.027300499571703267
# expected discounted reward bound: 3503.0303030302975
# value iteration: None
# proven optimal: False
# runtime: 1200.7653920650482
######################## Parameters ########################
# depth: 7
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(col, c1, c2, x1, s1, slot1, backoff1, bc1, x2, s2, slot2, backoff2, bc2):
    if bc2 <= 1.0:
        return 'station2_cmd_74'
    else:
        if bc2 <= 1.0:
            return 'station2_cmd_74'
        else:
            if bc2 <= 1.0:
                return 'time'
            else:
                if bc2 <= 1.0:
                    return 'time'
                else:
                    if bc2 <= 1.0:
                        return 'time'
                    else:
                        if bc2 <= 1.0:
                            return 'time'
                        else:
                            if bc2 <= 1.0:
                                return 'time'
                            else:
                                return 'station2_cmd_59'
