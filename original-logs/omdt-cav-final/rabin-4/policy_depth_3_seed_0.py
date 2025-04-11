######################## Properties ########################
# expected discounted reward: 93.00512622134539
# expected discounted reward bound: 96.05960099999989
# value iteration: None
# proven optimal: False
# runtime: 1200.1106369495392
######################## Parameters ########################
# depth: 3
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(c, b, r, p1, b1, r1, draw1, p2, b2, r2, draw2, p3, b3, r3, draw3, p4, b4, r4, draw4):
    if draw4 <= 1.0:
        if b4 <= 4.0:
            if r <= 0.0:
                return 'process1_cmd_0'
            else:
                return 'process4_cmd_18'
        else:
            if b4 <= 4.0:
                return 'process4_cmd_18'
            else:
                return 'process1_cmd_0'
    else:
        if draw4 <= 1.0:
            return 'process4_cmd_16'
        else:
            return 'process1_cmd_0'
