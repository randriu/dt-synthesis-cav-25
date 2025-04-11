######################## Properties ########################
# expected discounted reward: -98.95492583298613
# expected discounted reward bound: -47.71054798325503
# value iteration: None
# proven optimal: False
# runtime: 1200.0393550395966
######################## Parameters ########################
# depth: 3
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(gold, gem, attacked, x, y, required_gold, required_gem):
    if x <= 2.0:
        if y <= 1.0:
            return 'down'
        else:
            if x <= 1.0:
                return 'down'
            else:
                return 'left'
    else:
        if x <= 4.0:
            return '__random__'
        else:
            return 'top'
