######################## Properties ########################
# expected discounted reward: 967.889635027946
# expected discounted reward bound: 967.8976270858082
# value iteration: None
# proven optimal: True
# runtime: 450.75859689712524
######################## Parameters ########################
# depth: 4
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(inventory):
    if inventory <= 4.0:
        if inventory <= 3.0:
            if inventory <= 1.0:
                if inventory <= 0.0:
                    return '(Buy_12)'
                else:
                    return '(Buy_11)'
            else:
                if inventory <= 2.0:
                    return '(Buy_9)'
                else:
                    return '(Buy_8)'
        else:
            if inventory <= 14.0:
                return '(Buy_7)'
            else:
                return '(Don't'
    else:
        if inventory <= 5.0:
            return '(Buy_6)'
        else:
            if inventory <= 6.0:
                return '(Buy_5)'
            else:
                if inventory <= 8.0:
                    return '(Buy_3)'
                else:
                    return '(Buy_1)'
