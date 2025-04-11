######################## Properties ########################
# expected discounted reward: 6.025459502563179e-06
# expected discounted reward bound: 6.025459502563179e-06
# value iteration: None
# proven optimal: True
# runtime: 4.3487489223480225
######################## Parameters ########################
# depth: 1
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(x, y, z):
    if z <= 3.0:
        return '__random__'
    else:
        return '(up)'
