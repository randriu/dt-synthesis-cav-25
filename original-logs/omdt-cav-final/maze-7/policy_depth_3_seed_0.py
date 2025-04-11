######################## Properties ########################
# expected discounted reward: 2.8204902417497246
# expected discounted reward bound: 5.179580289184571
# value iteration: None
# proven optimal: False
# runtime: 1200.032485961914
######################## Parameters ########################
# depth: 3
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(picked0, picked1, picked2, picked3, picked4, picked5, picked6, x, y):
    if y <= 5.0:
        if y <= 0.0:
            return 'u'
        else:
            if x <= 13.0:
                return '__random__'
            else:
                return 'l'
    else:
        if picked5 <= 0.0:
            if y <= 6.0:
                return 'r'
            else:
                return 'u'
        else:
            if x <= 7.0:
                return 'r'
            else:
                return 'd'
