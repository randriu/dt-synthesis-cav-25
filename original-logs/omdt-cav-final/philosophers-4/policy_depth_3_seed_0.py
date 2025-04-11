######################## Properties ########################
# expected discounted reward: 88.60557102098613
# expected discounted reward bound: 94.86579510798335
# value iteration: None
# proven optimal: False
# runtime: 1200.14972615242
######################## Parameters ########################
# depth: 3
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(p1, p2, p3, p4):
    if p1 <= 0.0:
        if p2 <= 0.0:
            if p4 <= 0.0:
                return '__random__'
            else:
                return 'phil4_cmd_56'
        else:
            if p4 <= 8.0:
                return 'phil2_cmd_20'
            else:
                return 'phil4_cmd_66'
    else:
        if p4 <= 8.0:
            return 'phil1_cmd_2'
        else:
            return 'phil4_cmd_66'
