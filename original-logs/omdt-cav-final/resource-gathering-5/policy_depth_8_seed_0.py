######################## Properties ########################
# expected discounted reward: -99.99999948988302
# expected discounted reward bound: -47.710547983255005
# value iteration: None
# proven optimal: False
# runtime: 1200.335793018341
######################## Parameters ########################
# depth: 8
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(gold, gem, attacked, x, y, required_gold, required_gem):
    if required_gem <= 5.0:
        return 'down'
    else:
        return 'right'
