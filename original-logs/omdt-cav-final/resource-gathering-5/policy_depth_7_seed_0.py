######################## Properties ########################
# expected discounted reward: -99.91117157687793
# expected discounted reward bound: -47.71054798325502
# value iteration: None
# proven optimal: False
# runtime: 1200.2438089847565
######################## Parameters ########################
# depth: 7
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(gold, gem, attacked, x, y, required_gold, required_gem):
    if required_gold <= 0.0:
        if y <= 2.0:
            if required_gem <= 5.0:
                if required_gem <= 1.0:
                    return 'left'
                else:
                    return 'right'
            else:
                return 'right'
        else:
            if required_gem <= 5.0:
                return 'left'
            else:
                return 'right'
    else:
        if required_gem <= 5.0:
            if x <= 2.0:
                return 'right'
            else:
                return '__random__'
        else:
            return 'right'
