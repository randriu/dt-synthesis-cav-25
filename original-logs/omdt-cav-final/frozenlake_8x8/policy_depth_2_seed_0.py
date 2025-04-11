######################## Properties ########################
# expected discounted reward: 0.3870229821587146
# expected discounted reward bound: 0.3870229821587146
# value iteration: None
# proven optimal: True
# runtime: 3.539844036102295
######################## Parameters ########################
# depth: 2
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(X, Y):
    if Y <= 0.0:
        if X <= 0.0:
            return '(Up)'
        else:
            return '(Right)'
    else:
        if X <= 5.0:
            return '(Up)'
        else:
            return '(Right)'
