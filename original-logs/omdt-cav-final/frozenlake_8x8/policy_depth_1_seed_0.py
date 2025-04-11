######################## Properties ########################
# expected discounted reward: 0.306870983259296
# expected discounted reward bound: 0.306870983259296
# value iteration: None
# proven optimal: True
# runtime: 0.4564979076385498
######################## Parameters ########################
# depth: 1
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(X, Y):
    if X <= 4.0:
        return '(Up)'
    else:
        return '(Right)'
