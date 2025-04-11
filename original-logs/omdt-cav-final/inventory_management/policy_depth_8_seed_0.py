######################## Properties ########################
# expected discounted reward: 965.9989275334639
# expected discounted reward bound: 967.8976270892679
# value iteration: None
# proven optimal: False
# runtime: 1200.3809158802032
######################## Parameters ########################
# depth: 8
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(inventory):
    if inventory <= 55.0:
        if inventory <= 10.0:
            if inventory <= 6.0:
                if inventory <= 2.0:
                    if inventory <= 0.0:
                        return '(Buy_12)'
                    else:
                        return '(Buy_10)'
                else:
                    if inventory <= 3.0:
                        return '(Buy_8)'
                    else:
                        return '(Buy_7)'
            else:
                if inventory <= 73.0:
                    if inventory <= 8.0:
                        return '(Buy_2)'
                    else:
                        return '(Buy_1)'
                else:
                    return '(Don't'
        else:
            if inventory <= 14.0:
                if inventory <= 34.0:
                    if inventory <= 11.0:
                        return '(Buy_1)'
                    else:
                        return '(Buy_2)'
                else:
                    return '(Don't'
            else:
                if inventory <= 24.0:
                    return '(Don't'
                else:
                    if inventory <= 44.0:
                        return '(Buy_1)'
                    else:
                        if inventory <= 71.0:
                            return '__random__'
                        else:
                            return '(Don't'
    else:
        if inventory <= 5.0:
            return '(Don't'
        else:
            if inventory <= 100.0:
                if inventory <= 52.0:
                    return '(Don't'
                else:
                    if inventory <= 55.0:
                        return '(Buy_1)'
                    else:
                        if inventory <= 52.0:
                            return '(Don't'
                        else:
                            return '__random__'
            else:
                return '(Don't'
