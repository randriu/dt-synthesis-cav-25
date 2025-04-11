######################## Properties ########################
# expected discounted reward: 0.3518546075461676
# expected discounted reward bound: 0.3518546075461676
# value iteration: None
# proven optimal: True
# runtime: 68.51291298866272
######################## Parameters ########################
# depth: 3
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(x, y, z):
    if x <= 2.0:
        if z <= 0.0:
            if x <= 1.0:
                return '(right)'
            else:
                return '(forward)'
        else:
            return '(right)'
    else:
        if y <= 3.0:
            if z <= 2.0:
                return '(forward)'
            else:
                return '(up)'
        else:
            if z <= 3.0:
                return '(forward)'
            else:
                return '(right)'
