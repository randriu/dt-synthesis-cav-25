######################## Properties ########################
# expected discounted reward: 966.8791444979104
# expected discounted reward bound: 967.8976270892697
# value iteration: None
# proven optimal: False
# runtime: 1200.0070431232452
######################## Parameters ########################
# depth: 3
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(inventory):
    if inventory <= 4.0:
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
        if inventory <= 7.0:
            return '(Buy_5)'
        else:
            if inventory <= 69.0:
                return '(Buy_1)'
            else:
                return '(Don't'
