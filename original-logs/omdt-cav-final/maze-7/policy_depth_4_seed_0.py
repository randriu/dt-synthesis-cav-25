######################## Properties ########################
# expected discounted reward: 2.0543648309675078
# expected discounted reward bound: 5.179578905959841
# value iteration: None
# proven optimal: False
# runtime: 1200.0172371864319
######################## Parameters ########################
# depth: 4
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(picked0, picked1, picked2, picked3, picked4, picked5, picked6, x, y):
    if y <= 3.0:
        if picked1 <= 0.0:
            if picked0 <= 0.0:
                return 'l'
            else:
                return 'r'
        else:
            if x <= 9.0:
                return 'u'
            else:
                return 'l'
    else:
        if y <= 3.0:
            if picked4 <= 0.0:
                return 'u'
            else:
                if x <= 11.0:
                    return 'l'
                else:
                    return 'r'
        else:
            if picked2 <= 0.0:
                if picked6 <= 0.0:
                    return 'r'
                else:
                    return 'd'
            else:
                if x <= 5.0:
                    return '__random__'
                else:
                    return 'u'
