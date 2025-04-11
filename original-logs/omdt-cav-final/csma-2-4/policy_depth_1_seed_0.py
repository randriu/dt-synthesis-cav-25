######################## Properties ########################
# expected discounted reward: 38.82917578809692
# expected discounted reward bound: 39.19103308380171
# value iteration: None
# proven optimal: False
# runtime: 1200.0225720405579
######################## Parameters ########################
# depth: 1
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(b, y1, y2, s1, x1, bc1, cd1, s2, x2, bc2, cd2):
    if b <= 1.0:
        return 'send1'
    else:
        return 'cd'
