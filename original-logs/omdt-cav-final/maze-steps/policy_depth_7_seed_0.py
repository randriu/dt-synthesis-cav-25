######################## Properties ########################
# expected discounted reward: -17.19407060784086
# expected discounted reward bound: -17.15949222656103
# value iteration: None
# proven optimal: False
# runtime: 1200.0903310775757
######################## Parameters ########################
# depth: 7
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(picked0, picked1, picked2, x, y):
    if x <= 5.0:
        if picked2 <= 0.0:
            if x <= 2.0:
                if picked1 <= 0.0:
                    if x <= 1.0:
                        if x <= 0.0:
                            if y <= 4.0:
                                return 'u'
                            else:
                                return 'r'
                        else:
                            if y <= 2.0:
                                return 'u'
                            else:
                                return 'r'
                    else:
                        if y <= 2.0:
                            if y <= 0.0:
                                return 'u'
                            else:
                                return '__random__'
                        else:
                            if y <= 4.0:
                                return 'u'
                            else:
                                return 'd'
                else:
                    return '__random__'
            else:
                if x <= 4.0:
                    if x <= 3.0:
                        if y <= 4.0:
                            return 'u'
                        else:
                            return 'l'
                    else:
                        if y <= 5.0:
                            if y <= 2.0:
                                return 'u'
                            else:
                                return 'l'
                        else:
                            return 'r'
                else:
                    if x <= 4.0:
                        return '__random__'
                    else:
                        if y <= 5.0:
                            if y <= 3.0:
                                return 'l'
                            else:
                                return 'd'
                        else:
                            return '__random__'
        else:
            if x <= 1.0:
                if picked2 <= 0.0:
                    return '__random__'
                else:
                    if y <= 3.0:
                        if y <= 1.0:
                            if y <= 0.0:
                                return 'u'
                            else:
                                return 'r'
                        else:
                            if x <= 0.0:
                                return 'r'
                            else:
                                return 'd'
                    else:
                        if y <= 5.0:
                            if x <= 0.0:
                                return 'd'
                            else:
                                return 'r'
                        else:
                            return '__random__'
            else:
                if y <= 1.0:
                    if y <= 0.0:
                        if picked0 <= 0.0:
                            if x <= 4.0:
                                return 'r'
                            else:
                                return 'u'
                        else:
                            return 'u'
                    else:
                        if x <= 3.0:
                            if x <= 2.0:
                                return 'd'
                            else:
                                return 'l'
                        else:
                            return 'r'
                else:
                    if y <= 3.0:
                        if x <= 2.0:
                            return 'r'
                        else:
                            if x <= 4.0:
                                return 'd'
                            else:
                                return 'l'
                    else:
                        if y <= 5.0:
                            return 'd'
                        else:
                            return '__random__'
    else:
        if y <= 1.0:
            if y <= 0.0:
                return '__random__'
            else:
                if y <= 1.0:
                    if picked2 <= 0.0:
                        return 'l'
                    else:
                        return '__random__'
                else:
                    return '__random__'
        else:
            if x <= 5.0:
                return '__random__'
            else:
                if picked1 <= 0.0:
                    if x <= 6.0:
                        return 'l'
                    else:
                        if y <= 3.0:
                            return 'u'
                        else:
                            return 'l'
                else:
                    if x <= 6.0:
                        if y <= 2.0:
                            return 'u'
                        else:
                            return 'd'
                    else:
                        if y <= 5.0:
                            return 'u'
                        else:
                            return '__random__'
