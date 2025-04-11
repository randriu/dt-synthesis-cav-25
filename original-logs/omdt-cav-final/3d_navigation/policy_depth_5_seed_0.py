######################## Properties ########################
# expected discounted reward: 0.3518546075461697
# expected discounted reward bound: 0.3518546075461697
# value iteration: None
# proven optimal: True
# runtime: 82.68075299263
######################## Parameters ########################
# depth: 5
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(x, y, z):
    if z <= 3.0:
        if z <= 0.0:
            if x <= 1.0:
                if y <= 0.0:
                    return '(right)'
                else:
                    return '(backward)'
            else:
                if x <= 2.0:
                    return '(forward)'
                else:
                    return '__random__'
        else:
            if x <= 2.0:
                return '(right)'
            else:
                if y <= 3.0:
                    if z <= 2.0:
                        return '(forward)'
                    else:
                        return '(up)'
                else:
                    if x <= 2.0:
                        return '(right)'
                    else:
                        return '(forward)'
    else:
        if y <= 2.0:
            if z <= 4.0:
                if y <= 1.0:
                    if x <= 0.0:
                        return '(right)'
                    else:
                        return '(up)'
                else:
                    if y <= 1.0:
                        return '(left)'
                    else:
                        return '(right)'
            else:
                if x <= 2.0:
                    return '(left)'
                else:
                    return '(right)'
        else:
            if x <= 3.0:
                return '(right)'
            else:
                if x <= 3.0:
                    return '(right)'
                else:
                    return '(up)'
