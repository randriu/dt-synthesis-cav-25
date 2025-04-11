######################## Properties ########################
# expected discounted reward: 0.6555704167851438
# expected discounted reward bound: 0.96059601
# value iteration: None
# proven optimal: False
# runtime: 1200.1412150859833
######################## Parameters ########################
# depth: 4
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(p0, p1, p2):
    if p2 <= 15.0:
        if p0 <= 5.0:
            return 'process2_cmd_71'
        else:
            if p1 <= 3.0:
                return 'process2_cmd_71'
            else:
                return 'process1_cmd_32'
    else:
        if p2 <= 15.0:
            return 'process2_cmd_71'
        else:
            return 'process0_cmd_2'
