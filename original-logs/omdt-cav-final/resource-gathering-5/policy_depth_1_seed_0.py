######################## Properties ########################
# expected discounted reward: -95.14073751846024
# expected discounted reward bound: -95.13990466988768
# value iteration: None
# proven optimal: True
# runtime: 486.49770498275757
######################## Parameters ########################
# depth: 1
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(gold, gem, attacked, x, y, required_gold, required_gem):
    if gem <= 0.0:
        return 'top'
    else:
        return 'down'
