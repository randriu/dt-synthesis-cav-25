######################## Properties ########################
# expected discounted reward: 91.83062124607963
# expected discounted reward bound: 96.05960099999923
# value iteration: None
# proven optimal: False
# runtime: 1200.3315241336823
######################## Parameters ########################
# depth: 4
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(c, b, r, p1, b1, r1, draw1, p2, b2, r2, draw2, p3, b3, r3, draw3, p4, b4, r4, draw4):
    if draw4 <= 1.0:
        if draw3 <= 0.0:
            if b1 <= 3.0:
                if b <= 0.0:
                    return 'process1_cmd_0'
                else:
                    return 'process3_cmd_11'
            else:
                if b2 <= 5.0:
                    return 'process4_cmd_18'
                else:
                    return '__random__'
        else:
            return 'process4_cmd_18'
    else:
        return 'process4_cmd_18'
