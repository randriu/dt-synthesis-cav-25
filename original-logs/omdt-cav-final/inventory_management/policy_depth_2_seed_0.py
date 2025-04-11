######################## Properties ########################
# expected discounted reward: 966.1644947905057
# expected discounted reward bound: 967.897627089268
# value iteration: None
# proven optimal: False
# runtime: 1200.0090818405151
######################## Parameters ########################
# depth: 2
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(inventory):
    if inventory <= 2.0:
        if inventory <= 0.0:
            return '(Buy_12)'
        else:
            return '(Buy_10)'
    else:
        if inventory <= 4.0:
            return '(Buy_8)'
        else:
            return '(Buy_5)'
