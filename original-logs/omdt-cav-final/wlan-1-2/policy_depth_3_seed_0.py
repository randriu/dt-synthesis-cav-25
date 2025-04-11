######################## Properties ########################
# expected discounted reward: 0.04201439746501561
# expected discounted reward bound: 0.10827098374814301
# value iteration: None
# proven optimal: False
# runtime: 1200.1951849460602
######################## Parameters ########################
# depth: 3
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(col, c1, c2, x1, s1, slot1, backoff1, bc1, x2, s2, slot2, backoff2, bc2):
    if c1 <= 1.0:
        if backoff1 <= 14.0:
            if c2 <= 1.0:
                return 'time'
            else:
                return 'station1_cmd_39'
        else:
            return 'station2_cmd_74'
    else:
        if col <= 1.0:
            if c2 <= 1.0:
                return 'finish1'
            else:
                return 'station2_cmd_74'
        else:
            if bc2 <= 1.0:
                return 'station1_cmd_19'
            else:
                return 'finish1'
