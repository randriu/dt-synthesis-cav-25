######################## Properties ########################
# expected discounted reward: 0.02066642863130449
# expected discounted reward bound: 0.02066642863130449
# value iteration: None
# proven optimal: True
# runtime: 102.31446099281311
######################## Parameters ########################
# depth: 2
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(x, y, z):
    if x <= 3.0:
        if y <= 0.0:
            return '(up)'
        else:
            return '(right)'
    else:
        if z <= 3.0:
            return '(forward)'
        else:
            return '(up)'
