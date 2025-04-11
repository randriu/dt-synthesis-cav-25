######################## Properties ########################
# expected discounted reward: 0.3518546075461676
# expected discounted reward bound: 0.3518546075461676
# value iteration: None
# proven optimal: True
# runtime: 149.7614061832428
######################## Parameters ########################
# depth: 8
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(x, y, z):
    if z <= 0.0:
        if x <= 0.0:
            if y <= 3.0:
                return '(right)'
            else:
                return '(down)'
        else:
            if x <= 0.0:
                if y <= 2.0:
                    return '(up)'
                else:
                    return '__random__'
            else:
                if y <= 0.0:
                    if x <= 2.0:
                        if x <= 1.0:
                            return '(right)'
                        else:
                            return '(forward)'
                    else:
                        return '__random__'
                else:
                    return '__random__'
    else:
        if z <= 1.0:
            if x <= 1.0:
                if y <= 0.0:
                    if z <= 1.0:
                        if z <= 0.0:
                            return '__random__'
                        else:
                            if z <= 0.0:
                                return '(forward)'
                            else:
                                return '(right)'
                    else:
                        return '(right)'
                else:
                    if y <= 0.0:
                        return '(forward)'
                    else:
                        return '(down)'
            else:
                if y <= 0.0:
                    if x <= 2.0:
                        if x <= 1.0:
                            return '__random__'
                        else:
                            return '(right)'
                    else:
                        if x <= 3.0:
                            return '(forward)'
                        else:
                            return '__random__'
                else:
                    return '__random__'
        else:
            if z <= 2.0:
                if y <= 0.0:
                    return '(forward)'
                else:
                    if x <= 0.0:
                        return '(down)'
                    else:
                        if y <= 2.0:
                            return '(backward)'
                        else:
                            return '(down)'
            else:
                if x <= 0.0:
                    if z <= 4.0:
                        return '(right)'
                    else:
                        return '__random__'
                else:
                    if x <= 2.0:
                        if x <= 1.0:
                            if z <= 4.0:
                                if y <= 3.0:
                                    return '(up)'
                                else:
                                    return '(left)'
                            else:
                                return '__random__'
                        else:
                            if z <= 4.0:
                                if y <= 3.0:
                                    return '(backward)'
                                else:
                                    return '(up)'
                            else:
                                return '__random__'
                    else:
                        if z <= 3.0:
                            if y <= 3.0:
                                return '(up)'
                            else:
                                return '(forward)'
                        else:
                            return '(right)'
