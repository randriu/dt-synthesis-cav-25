######################## Properties ########################
# expected discounted reward: -87.69588738093287
# expected discounted reward bound: -47.71054798325503
# value iteration: None
# proven optimal: False
# runtime: 1200.0550789833069
######################## Parameters ########################
# depth: 4
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(gold, gem, attacked, x, y, required_gold, required_gem):
    if gem <= 0.0:
        if required_gem <= 4.0:
            if x <= 2.0:
                if y <= 4.0:
                    return 'top'
                else:
                    return 'right'
            else:
                if required_gem <= 0.0:
                    return 'down'
                else:
                    return '__random__'
        else:
            if required_gold <= 4.0:
                if y <= 4.0:
                    return 'top'
                else:
                    return 'right'
            else:
                if gold <= 0.0:
                    return 'top'
                else:
                    return 'down'
    else:
        if required_gem <= 5.0:
            return 'down'
        else:
            if required_gem <= 5.0:
                return 'right'
            else:
                if required_gem <= 5.0:
                    return 'right'
                else:
                    return 'down'
