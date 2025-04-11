######################## Properties ########################
# expected discounted reward: -19.743070666004254
# expected discounted reward bound: -17.15948869402516
# value iteration: None
# proven optimal: False
# runtime: 1200.0056509971619
######################## Parameters ########################
# depth: 4
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(picked0, picked1, picked2, x, y):
    if y <= 0.0:
        if x <= 1.0:
            return 'u'
        else:
            if x <= 4.0:
                if picked2 <= 0.0:
                    return 'u'
                else:
                    return 'r'
            else:
                return 'u'
    else:
        if picked2 <= 0.0:
            if y <= 4.0:
                if x <= 2.0:
                    return 'u'
                else:
                    return 'l'
            else:
                if x <= 1.0:
                    return 'r'
                else:
                    return 'd'
        else:
            if y <= 1.0:
                if x <= 2.0:
                    return 'd'
                else:
                    return 'r'
            else:
                if x <= 2.0:
                    return 'r'
                else:
                    return 'd'
