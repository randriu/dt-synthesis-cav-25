######################## Properties ########################
# expected discounted reward: -75.34320302123325
# expected discounted reward bound: -70.04494709788847
# value iteration: None
# proven optimal: False
# runtime: 1200.6656877994537
######################## Parameters ########################
# depth: 7
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(w12, y1, y2, x1, s1, w21, z1, z2, x2, s2):
    if s2 <= 7.0:
        if x2 <= 160.0:
            if x1 <= 164.0:
                if s1 <= 6.0:
                    if x2 <= 155.0:
                        if x1 <= 158.0:
                            if s2 <= 6.0:
                                return 'time'
                            else:
                                return 'snd_ack21'
                        else:
                            if x1 <= 160.0:
                                return 'snd_ack12'
                            else:
                                return 'time'
                    else:
                        if x2 <= 159.0:
                            return 'time'
                        else:
                            if x1 <= 160.0:
                                return 'time'
                            else:
                                return 'snd_idle21'
                else:
                    return 'rec_ack12'
            else:
                if x1 <= 164.0:
                    if x1 <= 164.0:
                        return 'rec_ack12'
                    else:
                        return 'snd_idle12'
                else:
                    if x1 <= 164.0:
                        return 'rec_ack12'
                    else:
                        if x1 <= 165.0:
                            return 'rec_req21'
                        else:
                            return 'snd_ack12'
        else:
            if x2 <= 164.0:
                if x2 <= 162.0:
                    if x1 <= 160.0:
                        return 'snd_idle12'
                    else:
                        return 'time'
                else:
                    if y2 <= 0.0:
                        return 'snd_req21'
                    else:
                        return 'snd_idle12'
            else:
                if x2 <= 164.0:
                    return 'time'
                else:
                    if x2 <= 165.0:
                        if x1 <= 163.0:
                            return 'snd_ack21'
                        else:
                            return 'rec_idle21'
                    else:
                        return 'time'
    else:
        if s2 <= 8.0:
            return 'snd_idle12'
        else:
            if s2 <= 8.0:
                return 'snd_idle12'
            else:
                if s2 <= 8.0:
                    return 'snd_idle12'
                else:
                    if s2 <= 8.0:
                        return 'snd_idle21'
                    else:
                        if s2 <= 8.0:
                            return 'time'
                        else:
                            return 'snd_idle12'
