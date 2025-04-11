######################## Properties ########################
# expected discounted reward: -63.22485151648766
# expected discounted reward bound: -63.22485151648766
# value iteration: None
# proven optimal: True
# runtime: 4.0637757778167725
######################## Parameters ########################
# depth: 1
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(picked0, picked1, picked2, x, y):
    if picked2 <= 0.0:
        return 'u'
    else:
        return 'd'
