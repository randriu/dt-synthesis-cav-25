######################## Properties ########################
# expected discounted reward: 1.4566473057155407
# expected discounted reward bound: 5.179579205593966
# value iteration: None
# proven optimal: False
# runtime: 1200.1397769451141
######################## Parameters ########################
# depth: 6
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(picked0, picked1, picked2, picked3, picked4, picked5, picked6, x, y):
    if y <= 6.0:
        if x <= 6.0:
            if y <= 0.0:
                if picked0 <= 0.0:
                    return 'r'
                else:
                    return '__random__'
            else:
                if y <= 4.0:
                    if x <= 0.0:
                        return 'l'
                    else:
                        return '__random__'
                else:
                    return 'r'
        else:
            if x <= 10.0:
                if picked4 <= 0.0:
                    return 'r'
                else:
                    if y <= 0.0:
                        return 'd'
                    else:
                        return 'r'
            else:
                return '__random__'
    else:
        if picked4 <= 0.0:
            if y <= 2.0:
                if picked1 <= 0.0:
                    return '__random__'
                else:
                    if y <= 1.0:
                        return 'd'
                    else:
                        return '__random__'
            else:
                if y <= 4.0:
                    if x <= 5.0:
                        return 'r'
                    else:
                        return '__random__'
                else:
                    if y <= 4.0:
                        return 'u'
                    else:
                        return '__random__'
        else:
            if x <= 7.0:
                if x <= 3.0:
                    return '__random__'
                else:
                    if picked6 <= 0.0:
                        return '__random__'
                    else:
                        return 'u'
            else:
                if picked2 <= 0.0:
                    if y <= 1.0:
                        return 'd'
                    else:
                        return '__random__'
                else:
                    if y <= 6.0:
                        return 'r'
                    else:
                        return 'l'
