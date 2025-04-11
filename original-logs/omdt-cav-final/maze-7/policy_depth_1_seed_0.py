######################## Properties ########################
# expected discounted reward: 1.9468852018047347
# expected discounted reward bound: 1.9468852018047347
# value iteration: None
# proven optimal: True
# runtime: 141.9096701145172
######################## Parameters ########################
# depth: 1
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(picked0, picked1, picked2, picked3, picked4, picked5, picked6, x, y):
    if x <= 7.0:
        return 'r'
    else:
        return '__random__'
