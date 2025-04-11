######################## Properties ########################
# expected discounted reward: -85.39771384765571
# expected discounted reward bound: -47.71054798325502
# value iteration: None
# proven optimal: False
# runtime: 1200.010115146637
######################## Parameters ########################
# depth: 2
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(gold, gem, attacked, x, y, required_gold, required_gem):
    if y <= 4.0:
        if x <= 4.0:
            return 'down'
        else:
            return 'top'
    else:
        if gold <= 0.0:
            return 'left'
        else:
            return 'down'
