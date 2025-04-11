######################## Properties ########################
# expected discounted reward: 39.00957653031921
# expected discounted reward bound: 39.19103308390617
# value iteration: None
# proven optimal: False
# runtime: 1200.4916689395905
######################## Parameters ########################
# depth: 4
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(b, y1, y2, s1, x1, bc1, cd1, s2, x2, bc2, cd2):
    if x1 <= 25.0:
        if b <= 1.0:
            if x1 <= 0.0:
                if cd1 <= 1.0:
                    return 'send1'
                else:
                    return 'time'
            else:
                return 'time'
        else:
            if b <= 1.0:
                return 'time'
            else:
                if b <= 1.0:
                    return 'busy2'
                else:
                    return 'cd'
    else:
        if cd2 <= 4.0:
            return 'end1'
        else:
            if cd2 <= 4.0:
                return 'time'
            else:
                if cd2 <= 4.0:
                    return '__random__'
                else:
                    return 'station1_cmd_21'
