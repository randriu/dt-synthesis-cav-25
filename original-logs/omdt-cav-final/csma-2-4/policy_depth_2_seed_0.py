######################## Properties ########################
# expected discounted reward: 39.19103308390623
# expected discounted reward bound: 39.19103308390623
# value iteration: None
# proven optimal: True
# runtime: 1144.4796071052551
######################## Parameters ########################
# depth: 2
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(b, y1, y2, s1, x1, bc1, cd1, s2, x2, bc2, cd2):
    if y1 <= 1.0:
        if b <= 1.0:
            return 'send1'
        else:
            return 'cd'
    else:
        if s1 <= 2.0:
            return 'end1'
        else:
            return 'end2'
