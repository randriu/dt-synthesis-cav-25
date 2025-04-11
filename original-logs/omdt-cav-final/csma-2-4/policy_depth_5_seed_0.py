######################## Properties ########################
# expected discounted reward: 0.3851938906681756
# expected discounted reward bound: 39.19103308390621
# value iteration: None
# proven optimal: False
# runtime: 1200.3236949443817
######################## Parameters ########################
# depth: 5
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(b, y1, y2, s1, x1, bc1, cd1, s2, x2, bc2, cd2):
    if cd2 <= 4.0:
        return 'station2_cmd_36'
    else:
        if cd2 <= 4.0:
            return 'send1'
        else:
            if cd2 <= 4.0:
                return 'send1'
            else:
                if cd2 <= 4.0:
                    return 'send1'
                else:
                    if cd2 <= 4.0:
                        return 'send1'
                    else:
                        return 'send2'
