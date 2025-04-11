######################## Properties ########################
# expected discounted reward: -73.36184963347286
# expected discounted reward bound: -70.04494709789223
# value iteration: None
# proven optimal: False
# runtime: 1200.0634548664093
######################## Parameters ########################
# depth: 2
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(w12, y1, y2, x1, s1, w21, z1, z2, x2, s2):
    if s1 <= 0.0:
        if s2 <= 0.0:
            return 'snd_idle21'
        else:
            return 'rec_idle21'
    else:
        if x1 <= 103.0:
            return 'rec_req12'
        else:
            return 'snd_idle12'
