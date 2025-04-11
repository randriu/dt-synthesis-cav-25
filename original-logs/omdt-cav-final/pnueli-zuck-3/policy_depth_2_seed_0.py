######################## Properties ########################
# expected discounted reward: 0.6019355945436087
# expected discounted reward bound: 0.96059601
# value iteration: None
# proven optimal: False
# runtime: 1200.1985321044922
######################## Parameters ########################
# depth: 2
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(p0, p1, p2):
    if p2 <= 14.0:
        return 'process0_cmd_2'
    else:
        if p0 <= 5.0:
            return 'process0_cmd_9'
        else:
            return 'process2_cmd_71'
