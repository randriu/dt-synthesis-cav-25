######################## Properties ########################
# expected discounted reward: 38.5194085884932
# expected discounted reward bound: 39.19103308390588
# value iteration: None
# proven optimal: False
# runtime: 1200.0826289653778
######################## Parameters ########################
# depth: 3
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(b, y1, y2, s1, x1, bc1, cd1, s2, x2, bc2, cd2):
    if b <= 1.0:
        if y2 <= 0.0:
            if x1 <= 29.0:
                return 'send1'
            else:
                return 'time'
        else:
            return 'time'
    else:
        if b <= 1.0:
            return 'time'
        else:
            if cd2 <= 4.0:
                return 'send1'
            else:
                return 'time'
