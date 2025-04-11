######################## Properties ########################
# expected discounted reward: 967.3255282797965
# expected discounted reward bound: 967.8976270842317
# value iteration: None
# proven optimal: False
# runtime: 1200.0245270729065
######################## Parameters ########################
# depth: 5
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(inventory):
    if inventory <= 9.0:
        if inventory <= 3.0:
            if inventory <= 2.0:
                if inventory <= 1.0:
                    if inventory <= 0.0:
                        return '(Buy_12)'
                    else:
                        return '(Buy_11)'
                else:
                    return '(Buy_9)'
            else:
                return '(Buy_8)'
        else:
            if inventory <= 5.0:
                return '(Buy_7)'
            else:
                return '(Buy_4)'
    else:
        if inventory <= 47.0:
            if inventory <= 20.0:
                return '(Buy_1)'
            else:
                if inventory <= 38.0:
                    return '(Buy_2)'
                else:
                    return '(Buy_1)'
        else:
            if inventory <= 95.0:
                if inventory <= 57.0:
                    return '(Don't'
                else:
                    if inventory <= 62.0:
                        return '(Don't'
                    else:
                        return '__random__'
            else:
                return '__random__'
