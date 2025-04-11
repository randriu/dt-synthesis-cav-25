######################## Properties ########################
# expected discounted reward: 0.3518546075461695
# expected discounted reward bound: 0.3518546075461695
# value iteration: None
# proven optimal: True
# runtime: 233.23830699920654
######################## Parameters ########################
# depth: 7
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
                if y <= 1.0:
                    return '(forward)'
                else:
                    if z <= 3.0:
                        if y <= 1.0:
                            return '(forward)'
                        else:
                            return '(right)'
                    else:
                        return '__random__'
        else:
            return '(right)'
    else:
        if x <= 2.0:
            if y <= 2.0:
                if z <= 4.0:
                    if x <= 1.0:
                        return '(backward)'
                    else:
                        return '__random__'
                else:
                    if z <= 4.0:
                        return '(left)'
                    else:
                        return '(right)'
            else:
                return '(right)'
        else:
            if x <= 3.0:
                if z <= 3.0:
                    if y <= 3.0:
                        if z <= 2.0:
                            return '(forward)'
                        else:
                            return '(up)'
                    else:
                        if y <= 3.0:
                            return '(up)'
                        else:
                            return '(forward)'
                else:
                    return '(right)'
            else:
                if z <= 4.0:
                    return '__random__'
                else:
                    return '(right)'
