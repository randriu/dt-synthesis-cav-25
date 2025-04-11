######################## Properties ########################
# expected discounted reward: 1.2484800281952466
# expected discounted reward bound: 5.179579264243873
# value iteration: None
# proven optimal: False
# runtime: 1200.129870891571
######################## Parameters ########################
# depth: 7
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(picked0, picked1, picked2, picked3, picked4, picked5, picked6, x, y):
    if y <= 6.0:
        if picked5 <= 0.0:
            if picked3 <= 0.0:
                if picked2 <= 0.0:
                    if y <= 0.0:
                        if picked6 <= 0.0:
                            return 'r'
                        else:
                            return '__random__'
                    else:
                        if picked6 <= 0.0:
                            return 'r'
                        else:
                            return '__random__'
                else:
                    if y <= 4.0:
                        if picked6 <= 0.0:
                            return 'l'
                        else:
                            return '__random__'
                    else:
                        if x <= 8.0:
                            if picked0 <= 0.0:
                                return 'u'
                            else:
                                return '__random__'
                        else:
                            if picked6 <= 0.0:
                                return '__random__'
                            else:
                                return 'r'
            else:
                if picked0 <= 0.0:
                    if y <= 2.0:
                        return '__random__'
                    else:
                        return 'l'
                else:
                    if x <= 4.0:
                        if y <= 5.0:
                            if x <= 2.0:
                                return 'l'
                            else:
                                return 'u'
                        else:
                            return 'u'
                    else:
                        if picked0 <= 0.0:
                            return 'u'
                        else:
                            return 'r'
        else:
            if picked3 <= 0.0:
                if picked5 <= 0.0:
                    if picked2 <= 0.0:
                        if y <= 5.0:
                            return 'l'
                        else:
                            return '__random__'
                    else:
                        if y <= 1.0:
                            return '__random__'
                        else:
                            return 'd'
                else:
                    if x <= 12.0:
                        if picked5 <= 0.0:
                            return 'l'
                        else:
                            return '__random__'
                    else:
                        if y <= 3.0:
                            return 'u'
                        else:
                            return 'd'
            else:
                if x <= 7.0:
                    if y <= 3.0:
                        if picked2 <= 0.0:
                            return '__random__'
                        else:
                            return 'd'
                    else:
                        if picked1 <= 0.0:
                            if picked5 <= 0.0:
                                return '__random__'
                            else:
                                return 'u'
                        else:
                            return 'd'
                else:
                    if y <= 2.0:
                        if picked3 <= 0.0:
                            return 'r'
                        else:
                            if picked6 <= 0.0:
                                return '__random__'
                            else:
                                return 'l'
                    else:
                        if picked6 <= 0.0:
                            if picked3 <= 0.0:
                                return 'r'
                            else:
                                return '__random__'
                        else:
                            return 'u'
    else:
        if picked6 <= 0.0:
            if picked1 <= 0.0:
                return '__random__'
            else:
                if x <= 9.0:
                    if picked0 <= 0.0:
                        return 'd'
                    else:
                        return 'l'
                else:
                    return '__random__'
        else:
            if x <= 10.0:
                if x <= 2.0:
                    if y <= 6.0:
                        return 'r'
                    else:
                        return '__random__'
                else:
                    return '__random__'
            else:
                if picked6 <= 0.0:
                    if picked3 <= 0.0:
                        return 'r'
                    else:
                        return 'l'
                else:
                    if y <= 6.0:
                        return 'u'
                    else:
                        return '__random__'
