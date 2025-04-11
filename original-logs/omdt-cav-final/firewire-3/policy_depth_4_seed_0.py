######################## Properties ########################
# expected discounted reward: -70.30583826865562
# expected discounted reward bound: -70.04494709789367
# value iteration: None
# proven optimal: False
# runtime: 1200.211655139923
######################## Parameters ########################
# depth: 4
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(w12, y1, y2, x1, s1, w21, z1, z2, x2, s2):
    if w21 <= 0.0:
        if w12 <= 1.0:
            if s1 <= 0.0:
                if s2 <= 5.0:
                    return 'snd_idle12'
                else:
                    return 'time'
            else:
                return 'snd_req21'
        else:
            if w12 <= 1.0:
                return 'time'
            else:
                if w12 <= 1.0:
                    return 'time'
                else:
                    return 'rec_ack12'
    else:
        if w21 <= 1.0:
            if w21 <= 0.0:
                return 'time'
            else:
                return 'rec_req21'
        else:
            if w21 <= 1.0:
                if s2 <= 6.0:
                    return 'snd_req21'
                else:
                    return 'time'
            else:
                if w12 <= 0.0:
                    return 'rec_ack21'
                else:
                    return 'rec_idle21'
