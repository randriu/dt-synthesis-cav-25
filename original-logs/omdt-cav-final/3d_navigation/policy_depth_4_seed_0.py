######################## Properties ########################
# expected discounted reward: 0.3518547724430858
# expected discounted reward bound: 0.3518547724430858
# value iteration: None
# proven optimal: True
# runtime: 42.54367709159851
######################## Parameters ########################
# depth: 4
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(x, y, z):
    if x <= 2.0:
        if y <= 0.0:
            if z <= 0.0:
                if x <= 1.0:
                    return '(right)'
                else:
                    return '(forward)'
            else:
                return '(right)'
        else:
            if z <= 0.0:
                return '(forward)'
            else:
                return '(right)'
    else:
        if y <= 3.0:
            if z <= 2.0:
                return '(forward)'
            else:
                if z <= 4.0:
                    return '(up)'
                else:
                    return '(backward)'
        else:
            if x <= 3.0:
                if z <= 3.0:
                    return '(forward)'
                else:
                    return '(right)'
            else:
                if z <= 4.0:
                    return '(up)'
                else:
                    return '(right)'
