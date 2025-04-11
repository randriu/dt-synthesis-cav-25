######################## Properties ########################
# expected discounted reward: -91.56907882345837
# expected discounted reward bound: -47.710547983255886
# value iteration: None
# proven optimal: False
# runtime: 1200.3548460006714
######################## Parameters ########################
# depth: 5
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(gold, gem, attacked, x, y, required_gold, required_gem):
    if gem <= 0.0:
        if x <= 2.0:
            if required_gold <= 2.0:
                if gold <= 0.0:
                    return 'top'
                else:
                    if required_gem <= 0.0:
                        return 'down'
                    else:
                        return 'top'
            else:
                if y <= 4.0:
                    return 'top'
                else:
                    return 'right'
        else:
            if x <= 2.0:
                return 'right'
            else:
                if x <= 4.0:
                    if required_gem <= 3.0:
                        return '__random__'
                    else:
                        return 'right'
                else:
                    if required_gem <= 3.0:
                        return 'down'
                    else:
                        return 'top'
    else:
        if required_gold <= 4.0:
            if gem <= 0.0:
                return 'right'
            else:
                if gold <= 0.0:
                    if required_gold <= 2.0:
                        return 'down'
                    else:
                        return 'top'
                else:
                    if gold <= 0.0:
                        return 'left'
                    else:
                        return 'down'
        else:
            if required_gold <= 4.0:
                if required_gem <= 5.0:
                    return 'top'
                else:
                    return 'right'
            else:
                if required_gem <= 5.0:
                    return 'down'
                else:
                    if required_gem <= 5.0:
                        return 'top'
                    else:
                        return 'right'
