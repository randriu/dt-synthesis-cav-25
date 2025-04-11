######################## Properties ########################
# expected discounted reward: 0.03829941550405779
# expected discounted reward bound: 0.10827098374814215
# value iteration: None
# proven optimal: False
# runtime: 1200.2193717956543
######################## Parameters ########################
# depth: 5
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(col, c1, c2, x1, s1, slot1, backoff1, bc1, x2, s2, slot2, backoff2, bc2):
    if s2 <= 2.0:
        if c1 <= 1.0:
            if x1 <= 0.0:
                if x2 <= 0.0:
                    if bc2 <= 1.0:
                        return 'station2_cmd_52'
                    else:
                        return 'time'
                else:
                    if bc2 <= 1.0:
                        return 'station2_cmd_42'
                    else:
                        return 'finish1'
            else:
                if s1 <= 10.0:
                    if x1 <= 0.0:
                        return 'station2_cmd_59'
                    else:
                        return 'station1_cmd_13'
                else:
                    return 'time'
        else:
            if bc2 <= 1.0:
                if c2 <= 1.0:
                    return 'station2_cmd_54'
                else:
                    return 'time'
            else:
                return 'time'
    else:
        if x1 <= 9.0:
            if bc1 <= 0.0:
                if x2 <= 8.0:
                    if c1 <= 1.0:
                        return 'station2_cmd_74'
                    else:
                        return 'time'
                else:
                    if x1 <= 6.0:
                        return 'finish2'
                    else:
                        return 'finish1'
            else:
                if s1 <= 4.0:
                    if s2 <= 7.0:
                        return 'station2_cmd_48'
                    else:
                        return 'station1_cmd_15'
                else:
                    return 'station2_cmd_74'
        else:
            if bc2 <= 1.0:
                if c2 <= 1.0:
                    if c1 <= 1.0:
                        return 'station2_cmd_74'
                    else:
                        return 'finish1'
                else:
                    if x2 <= 9.0:
                        return 'finish2'
                    else:
                        return 'time'
            else:
                if x2 <= 9.0:
                    if bc2 <= 1.0:
                        return 'time'
                    else:
                        return 'station1_cmd_24'
                else:
                    return 'time'
