######################## Properties ########################
# expected discounted reward: 0.02738727183000349
# expected discounted reward bound: 0.10827098374814134
# value iteration: None
# proven optimal: False
# runtime: 1200.459037065506
######################## Parameters ########################
# depth: 6
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(col, c1, c2, x1, s1, slot1, backoff1, bc1, x2, s2, slot2, backoff2, bc2):
    if bc2 <= 1.0:
        if backoff1 <= 5.0:
            if s2 <= 2.0:
                return 'station2_cmd_42'
            else:
                return 'station2_cmd_74'
        else:
            return 'station2_cmd_74'
    else:
        return 'time'
