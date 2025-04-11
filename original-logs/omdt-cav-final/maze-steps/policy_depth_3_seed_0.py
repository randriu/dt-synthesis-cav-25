######################## Properties ########################
# expected discounted reward: -19.989502101132487
# expected discounted reward bound: -17.159483056664403
# value iteration: None
# proven optimal: False
# runtime: 1200.00665807724
######################## Parameters ########################
# depth: 3
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(picked0, picked1, picked2, x, y):
    if x <= 2.0:
        if y <= 4.0:
            if picked2 <= 0.0:
                return 'u'
            else:
                return 'r'
        else:
            if x <= 1.0:
                return 'r'
            else:
                return 'd'
    else:
        if y <= 1.0:
            if y <= 0.0:
                return 'u'
            else:
                return 'r'
        else:
            if picked2 <= 0.0:
                return 'l'
            else:
                return 'd'
