######################## Properties ########################
# expected discounted reward: 0.23870831978803053
# expected discounted reward bound: 0.3486651695478028
# value iteration: None
# proven optimal: False
# runtime: 1200.0018949508667
######################## Parameters ########################
# depth: 3
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(X, Y):
    if X <= 1.0:
        if Y <= 7.0:
            if Y <= 6.0:
                return '(Left)'
            else:
                return '(Down)'
        else:
            if X <= 0.0:
                return '(Up)'
            else:
                return '(Right)'
    else:
        if Y <= 10.0:
            return '(Down)'
        else:
            if X <= 6.0:
                return '(Right)'
            else:
                return '(Left)'
