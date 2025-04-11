######################## Properties ########################
# expected discounted reward: 2.2366198444073357
# expected discounted reward bound: 5.179579236499448
# value iteration: None
# proven optimal: False
# runtime: 1200.022959947586
######################## Parameters ########################
# depth: 5
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(picked0, picked1, picked2, picked3, picked4, picked5, picked6, x, y):
    if x <= 0.0:
        if y <= 3.0:
            if picked5 <= 0.0:
                if y <= 1.0:
                    return 'd'
                else:
                    if y <= 1.0:
                        return 'u'
                    else:
                        return 'r'
            else:
                return 'u'
        else:
            if picked5 <= 0.0:
                if y <= 5.0:
                    return 'u'
                else:
                    return 'r'
            else:
                if picked5 <= 0.0:
                    return 'u'
                else:
                    if picked5 <= 0.0:
                        return 'd'
                    else:
                        return 'r'
    else:
        if y <= 3.0:
            if x <= 0.0:
                return 'u'
            else:
                if x <= 1.0:
                    if picked0 <= 0.0:
                        return 'u'
                    else:
                        return 'r'
                else:
                    if picked6 <= 0.0:
                        return 'r'
                    else:
                        return 'l'
        else:
            if x <= 2.0:
                if picked1 <= 0.0:
                    if picked3 <= 0.0:
                        return 'r'
                    else:
                        return '__random__'
                else:
                    return 'u'
            else:
                if x <= 2.0:
                    return 'u'
                else:
                    return 'd'
