######################## Properties ########################
# expected discounted reward: 0.11039830765513763
# expected discounted reward bound: 0.11039830765513763
# value iteration: None
# proven optimal: True
# runtime: 0.17445802688598633
######################## Parameters ########################
# depth: 1
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(X, Y):
    if Y <= 1.0:
        return '(Left)'
    else:
        return '(Down)'
