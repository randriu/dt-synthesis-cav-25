######################## Properties ########################
# expected discounted reward: -76.21458530853319
# expected discounted reward bound: -70.04494709789934
# value iteration: None
# proven optimal: False
# runtime: 1200.2388410568237
######################## Parameters ########################
# depth: 5
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(w12, y1, y2, x1, s1, w21, z1, z2, x2, s2):
    if x1 <= 166.0:
        if w12 <= 5.0:
            if s2 <= 8.0:
                if x2 <= 162.0:
                    if s2 <= 6.0:
                        return 'rec_idle12'
                    else:
                        return 'rec_ack21'
                else:
                    return 'rec_idle12'
            else:
                return 'time'
        else:
            if w12 <= 5.0:
                if x1 <= 162.0:
                    return 'rec_idle12'
                else:
                    if s2 <= 8.0:
                        return 'time'
                    else:
                        return 'snd_idle12'
            else:
                return 'time'
    else:
        if x2 <= 166.0:
            if s2 <= 8.0:
                return 'time'
            else:
                if s2 <= 8.0:
                    return 'time'
                else:
                    if s2 <= 8.0:
                        return 'snd_idle12'
                    else:
                        return 'time'
        else:
            if s2 <= 8.0:
                if x2 <= 166.0:
                    return 'snd_req12'
                else:
                    return 'time'
            else:
                if s2 <= 8.0:
                    return 'snd_idle12'
                else:
                    return 'time'
