######################## Properties ########################
# expected discounted reward: -24.555845464362722
# expected discounted reward bound: -24.555845464362722
# value iteration: None
# proven optimal: True
# runtime: 156.75258111953735
######################## Parameters ########################
# depth: 2
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(picked0, picked1, picked2, x, y):
    if picked2 <= 0.0:
        if y <= 4.0:
            return 'u'
        else:
            return 'r'
    else:
        if y <= 1.0:
            return 'r'
        else:
            return 'd'
