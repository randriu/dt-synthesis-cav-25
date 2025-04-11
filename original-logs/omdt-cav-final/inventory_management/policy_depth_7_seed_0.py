######################## Properties ########################
# expected discounted reward: 966.1022291209522
# expected discounted reward bound: 967.8976270888153
# value iteration: None
# proven optimal: False
# runtime: 1200.0749521255493
######################## Parameters ########################
# depth: 7
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(inventory):
    if inventory <= 39.0:
        if inventory <= 6.0:
            if inventory <= 2.0:
                if inventory <= 0.0:
                    return '(Buy_12)'
                else:
                    return '(Buy_10)'
            else:
                if inventory <= 4.0:
                    return '(Buy_8)'
                else:
                    return '(Buy_6)'
        else:
            if inventory <= 95.0:
                if inventory <= 22.0:
                    return '(Buy_1)'
                else:
                    if inventory <= 56.0:
                        return '(Buy_3)'
                    else:
                        return '(Don't'
            else:
                return '(Don't'
    else:
        if inventory <= 39.0:
            if inventory <= 38.0:
                if inventory <= 68.0:
                    return '__random__'
                else:
                    return '(Don't'
            else:
                if inventory <= 47.0:
                    return '__random__'
                else:
                    return '(Don't'
        else:
            if inventory <= 95.0:
                if inventory <= 57.0:
                    return '(Buy_78)'
                else:
                    return '__random__'
            else:
                if inventory <= 94.0:
                    return '(Buy_74)'
                else:
                    return '__random__'
