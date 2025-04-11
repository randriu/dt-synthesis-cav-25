######################## Properties ########################
# expected discounted reward: 0.044576632718176974
# expected discounted reward bound: 0.10827098374814301
# value iteration: None
# proven optimal: False
# runtime: 1200.0891020298004
######################## Parameters ########################
# depth: 2
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(col, c1, c2, x1, s1, slot1, backoff1, bc1, x2, s2, slot2, backoff2, bc2):
    if s1 <= 8.0:
        return 'time'
    else:
        if s2 <= 2.0:
            return 'station2_cmd_42'
        else:
            return 'time'
