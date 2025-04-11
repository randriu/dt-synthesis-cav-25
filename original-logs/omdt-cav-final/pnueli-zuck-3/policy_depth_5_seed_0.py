######################## Properties ########################
# expected discounted reward: 0.6561779545080005
# expected discounted reward bound: 0.96059601
# value iteration: None
# proven optimal: False
# runtime: 1200.2609281539917
######################## Parameters ########################
# depth: 5
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(p0, p1, p2):
    if p0 <= 0.0:
        if p2 <= 0.0:
            return 'process0_cmd_2'
        else:
            return 'process2_cmd_71'
    else:
        if p1 <= 0.0:
            return 'process2_cmd_71'
        else:
            if p0 <= 0.0:
                return 'process2_cmd_71'
            else:
                if p0 <= 0.0:
                    return 'process2_cmd_71'
                else:
                    if p2 <= 14.0:
                        return 'process2_cmd_55'
                    else:
                        return 'process2_cmd_71'
