######################## Properties ########################
# expected discounted reward: 0.6529688134082472
# expected discounted reward bound: 0.96059601
# value iteration: None
# proven optimal: False
# runtime: 1200.0814518928528
######################## Parameters ########################
# depth: 3
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(p0, p1, p2):
    if p2 <= 15.0:
        return 'process2_cmd_71'
    else:
        if p2 <= 15.0:
            return 'process0_cmd_2'
        else:
            if p2 <= 15.0:
                return 'process0_cmd_2'
            else:
                return 'process2_cmd_71'
