######################## Properties ########################
# expected discounted reward: -73.25349035606627
# expected discounted reward bound: -70.04494709795397
# value iteration: None
# proven optimal: False
# runtime: 1200.037458896637
######################## Parameters ########################
# depth: 3
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(w12, y1, y2, x1, s1, w21, z1, z2, x2, s2):
    if s2 <= 0.0:
        if w12 <= 0.0:
            if s1 <= 2.0:
                return 'snd_idle12'
            else:
                return 'snd_idle21'
        else:
            if w21 <= 5.0:
                return 'rec_idle12'
            else:
                return 'time'
    else:
        if w21 <= 1.0:
            return 'rec_req12'
        else:
            return 'rec_ack21'
