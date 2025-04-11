######################## Properties ########################
# expected discounted reward: -75.5371341472445
# expected discounted reward bound: -70.04494709788847
# value iteration: None
# proven optimal: False
# runtime: 1200.3225510120392
######################## Parameters ########################
# depth: 6
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(w12, y1, y2, x1, s1, w21, z1, z2, x2, s2):
    if x1 <= 75.0:
        if x2 <= 159.0:
            if x2 <= 158.0:
                if x2 <= 138.0:
                    if s2 <= 6.0:
                        if s1 <= 6.0:
                            return 'time'
                        else:
                            return 'rec_ack12'
                    else:
                        return 'rec_ack21'
                else:
                    if s2 <= 8.0:
                        return 'time'
                    else:
                        if s2 <= 8.0:
                            return 'snd_idle21'
                        else:
                            return 'snd_idle12'
            else:
                if s2 <= 8.0:
                    if y2 <= 2.0:
                        return 'rec_ack21'
                    else:
                        return 'time'
                else:
                    if s2 <= 8.0:
                        return 'snd_idle12'
                    else:
                        if s2 <= 8.0:
                            return 'snd_idle21'
                        else:
                            return 'snd_idle12'
        else:
            if x2 <= 166.0:
                if x2 <= 165.0:
                    if x2 <= 164.0:
                        return 'time'
                    else:
                        if x2 <= 164.0:
                            return 'snd_idle21'
                        else:
                            return 'rec_req12'
                else:
                    if s2 <= 8.0:
                        return 'snd_ack21'
                    else:
                        return 'snd_idle12'
            else:
                if x2 <= 166.0:
                    if s2 <= 8.0:
                        if y1 <= 2.0:
                            return 'rec_ack21'
                        else:
                            return 'snd_ack21'
                    else:
                        return 'snd_idle12'
                else:
                    if s2 <= 8.0:
                        return 'rec_ack21'
                    else:
                        return 'snd_idle12'
    else:
        if x1 <= 166.0:
            if x2 <= 164.0:
                if x2 <= 163.0:
                    if s2 <= 8.0:
                        if x1 <= 163.0:
                            return 'time'
                        else:
                            return 'snd_ack12'
                    else:
                        if s2 <= 8.0:
                            return 'time'
                        else:
                            return 'snd_idle12'
                else:
                    if s2 <= 8.0:
                        return 'snd_req12'
                    else:
                        if s2 <= 8.0:
                            return 'snd_idle12'
                        else:
                            return '__random__'
            else:
                if s2 <= 8.0:
                    return 'time'
                else:
                    return 'snd_idle12'
        else:
            if s2 <= 8.0:
                return 'time'
            else:
                if s2 <= 8.0:
                    return 'time'
                else:
                    if s2 <= 8.0:
                        return 'time'
                    else:
                        if s2 <= 8.0:
                            return 'snd_idle12'
                        else:
                            return 'snd_idle21'
