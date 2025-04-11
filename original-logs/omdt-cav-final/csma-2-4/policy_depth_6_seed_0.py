######################## Properties ########################
# expected discounted reward: 38.82811995686014
# expected discounted reward bound: 39.19103308389904
# value iteration: None
# proven optimal: False
# runtime: 1201.033889055252
######################## Parameters ########################
# depth: 6
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(b, y1, y2, s1, x1, bc1, cd1, s2, x2, bc2, cd2):
    if b <= 1.0:
        if y2 <= 0.0:
            if s1 <= 0.0:
                if b <= 0.0:
                    if cd2 <= 4.0:
                        return 'send1'
                    else:
                        return 'send2'
                else:
                    return 'station2_cmd_34'
            else:
                if x2 <= 29.0:
                    if cd2 <= 4.0:
                        return 'time'
                    else:
                        return 'station1_cmd_21'
                else:
                    if bc1 <= 13.0:
                        return 'end1'
                    else:
                        return 'station1_cmd_20'
        else:
            if y2 <= 0.0:
                if cd2 <= 4.0:
                    return 'station1_cmd_18'
                else:
                    if cd2 <= 4.0:
                        return 'time'
                    else:
                        if cd2 <= 4.0:
                            return 'send1'
                        else:
                            return '__random__'
            else:
                if cd2 <= 4.0:
                    return 'send1'
                else:
                    if cd2 <= 4.0:
                        return '__random__'
                    else:
                        if cd2 <= 4.0:
                            return 'time'
                        else:
                            return 'send1'
    else:
        if y2 <= 0.0:
            if cd2 <= 4.0:
                if b <= 1.0:
                    return 'send1'
                else:
                    return 'cd'
            else:
                if cd2 <= 4.0:
                    return 'time'
                else:
                    if cd2 <= 4.0:
                        return 'send2'
                    else:
                        if cd2 <= 4.0:
                            return 'send1'
                        else:
                            return 'send2'
        else:
            if y2 <= 0.0:
                if cd2 <= 4.0:
                    return 'send1'
                else:
                    if cd2 <= 4.0:
                        return 'end2'
                    else:
                        return 'send1'
            else:
                if y2 <= 0.0:
                    if cd2 <= 4.0:
                        return 'station2_cmd_33'
                    else:
                        return 'send1'
                else:
                    if cd2 <= 4.0:
                        return 'send2'
                    else:
                        if cd2 <= 4.0:
                            return 'time'
                        else:
                            return 'send1'
