######################## Properties ########################
# expected discounted reward: 88.45278375879359
# expected discounted reward bound: 94.62307437438267
# value iteration: None
# proven optimal: False
# runtime: 1200.1121151447296
######################## Parameters ########################
# depth: 2
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(p1, p2, p3, p4):
    if p2 <= 0.0:
        if p1 <= 0.0:
            return '__random__'
        else:
            return 'phil1_cmd_2'
    else:
        if p4 <= 8.0:
            return 'phil2_cmd_20'
        else:
            return '__random__'
