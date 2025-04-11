######################## Properties ########################
# expected discounted reward: 967.6258377235661
# expected discounted reward bound: 967.8976270892667
# value iteration: None
# proven optimal: False
# runtime: 1200.0646851062775
######################## Parameters ########################
# depth: 6
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(inventory):
    if inventory <= 57.0:
        if inventory <= 23.0:
            if inventory <= 4.0:
                if inventory <= 2.0:
                    if inventory <= 1.0:
                        if inventory <= 0.0:
                            return '(Buy_12)'
                        else:
                            return '(Buy_11)'
                    else:
                        return '(Buy_9)'
                else:
                    if inventory <= 3.0:
                        return '(Buy_8)'
                    else:
                        return '(Buy_7)'
            else:
                if inventory <= 22.0:
                    if inventory <= 6.0:
                        return '(Buy_6)'
                    else:
                        if inventory <= 19.0:
                            return '(Buy_3)'
                        else:
                            return '(Buy_7)'
                else:
                    if inventory <= 23.0:
                        return '__random__'
                    else:
                        return '(Don't'
        else:
            if inventory <= 93.0:
                return '(Buy_27)'
            else:
                return '(Don't'
    else:
        if inventory <= 63.0:
            if inventory <= 57.0:
                return '(Don't'
            else:
                if inventory <= 58.0:
                    return '(Buy_31)'
                else:
                    return '(Buy_13)'
        else:
            if inventory <= 80.0:
                if inventory <= 64.0:
                    return '(Buy_1)'
                else:
                    return '__random__'
            else:
                if inventory <= 100.0:
                    if inventory <= 83.0:
                        return '(Don't'
                    else:
                        return '__random__'
                else:
                    return '(Don't'
