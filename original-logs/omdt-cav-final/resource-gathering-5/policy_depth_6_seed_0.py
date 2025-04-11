######################## Properties ########################
# expected discounted reward: -96.76637361923471
# expected discounted reward bound: -47.71054798325502
# value iteration: None
# proven optimal: False
# runtime: 1200.0791988372803
######################## Parameters ########################
# depth: 6
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(gold, gem, attacked, x, y, required_gold, required_gem):
    if required_gold <= 3.0:
        if required_gem <= 4.0:
            if x <= 0.0:
                if y <= 0.0:
                    if gem <= 0.0:
                        return '__random__'
                    else:
                        return 'down'
                else:
                    return 'down'
            else:
                if y <= 4.0:
                    if x <= 0.0:
                        return 'down'
                    else:
                        if x <= 4.0:
                            return 'down'
                        else:
                            return 'top'
                else:
                    if x <= 0.0:
                        return 'right'
                    else:
                        if x <= 3.0:
                            return 'down'
                        else:
                            return 'left'
        else:
            return 'down'
    else:
        if required_gold <= 3.0:
            if required_gem <= 4.0:
                return 'right'
            else:
                if required_gem <= 5.0:
                    return 'right'
                else:
                    if required_gem <= 5.0:
                        return 'down'
                    else:
                        return 'right'
        else:
            if attacked <= 0.0:
                if required_gold <= 4.0:
                    if required_gold <= 3.0:
                        if required_gem <= 5.0:
                            return 'down'
                        else:
                            return 'right'
                    else:
                        if required_gem <= 4.0:
                            return 'down'
                        else:
                            return '__random__'
                else:
                    if gold <= 0.0:
                        if required_gem <= 4.0:
                            return 'down'
                        else:
                            return 'top'
                    else:
                        return 'down'
            else:
                if required_gem <= 5.0:
                    if y <= 0.0:
                        return 'right'
                    else:
                        return 'top'
                else:
                    if required_gem <= 5.0:
                        return 'down'
                    else:
                        if required_gem <= 5.0:
                            return 'top'
                        else:
                            return 'right'
