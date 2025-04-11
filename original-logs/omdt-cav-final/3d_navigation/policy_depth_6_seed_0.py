######################## Properties ########################
# expected discounted reward: 0.3518546075461676
# expected discounted reward bound: 0.3518546075461676
# value iteration: None
# proven optimal: True
# runtime: 82.05153298377991
######################## Parameters ########################
# depth: 6
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(x, y, z):
    if y <= 2.0:
        if x <= 2.0:
            if z <= 0.0:
                if x <= 1.0:
                    if y <= 0.0:
                        return '(right)'
                    else:
                        return '(forward)'
                else:
                    return '(forward)'
            else:
                if z <= 4.0:
                    return '(right)'
                else:
                    return '__random__'
        else:
            if x <= 2.0:
                if z <= 4.0:
                    return '(forward)'
                else:
                    return '__random__'
            else:
                if x <= 3.0:
                    if x <= 2.0:
                        return '(up)'
                    else:
                        if z <= 2.0:
                            return '(forward)'
                        else:
                            return '(up)'
                else:
                    if x <= 3.0:
                        return '__random__'
                    else:
                        if z <= 4.0:
                            return '(backward)'
                        else:
                            return '__random__'
    else:
        if x <= 2.0:
            if x <= 1.0:
                if y <= 2.0:
                    return '(up)'
                else:
                    if z <= 4.0:
                        return '(up)'
                    else:
                        return '__random__'
            else:
                if y <= 2.0:
                    if z <= 4.0:
                        return '(backward)'
                    else:
                        return '(forward)'
                else:
                    if z <= 4.0:
                        return '(backward)'
                    else:
                        return '__random__'
        else:
            if y <= 3.0:
                if y <= 2.0:
                    if x <= 1.0:
                        return '(forward)'
                    else:
                        return '(down)'
                else:
                    return '(up)'
            else:
                if y <= 3.0:
                    if x <= 2.0:
                        return '(down)'
                    else:
                        if z <= 0.0:
                            return '__random__'
                        else:
                            return '(left)'
                else:
                    if z <= 4.0:
                        if z <= 3.0:
                            return '(forward)'
                        else:
                            return '(right)'
                    else:
                        return '__random__'
