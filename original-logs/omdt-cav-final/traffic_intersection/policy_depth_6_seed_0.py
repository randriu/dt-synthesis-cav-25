######################## Properties ########################
# expected discounted reward: 2.1208072714010786
# expected discounted reward bound: 2.124566698376928
# value iteration: None
# proven optimal: False
# runtime: 1200.0105350017548
######################## Parameters ########################
# depth: 6
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(green_side, cars_left, cars_right, waiting_time):
    if green_side <= 0.0:
        if cars_left <= 4.0:
            if cars_left <= 2.0:
                if cars_left <= 1.0:
                    if cars_right <= 0.0:
                        if waiting_time <= 2.0:
                            return '(wait)'
                        else:
                            return '(switch_light)'
                    else:
                        return '(switch_light)'
                else:
                    if cars_right <= 1.0:
                        if waiting_time <= 3.0:
                            return '(wait)'
                        else:
                            return '(switch_light)'
                    else:
                        if waiting_time <= 2.0:
                            return '(wait)'
                        else:
                            return '(switch_light)'
            else:
                if cars_left <= 3.0:
                    if cars_right <= 1.0:
                        if waiting_time <= 2.0:
                            return '(wait)'
                        else:
                            return '(switch_light)'
                    else:
                        if waiting_time <= 1.0:
                            return '(wait)'
                        else:
                            return '(switch_light)'
                else:
                    if waiting_time <= 5.0:
                        if waiting_time <= 2.0:
                            return '(wait)'
                        else:
                            return '(switch_light)'
                    else:
                        if cars_right <= 4.0:
                            return '(switch_light)'
                        else:
                            return '__random__'
        else:
            if waiting_time <= 5.0:
                if cars_right <= 4.0:
                    if waiting_time <= 3.0:
                        return '(wait)'
                    else:
                        return '__random__'
                else:
                    return '(switch_light)'
            else:
                return '(switch_light)'
    else:
        if cars_left <= 3.0:
            if green_side <= 0.0:
                if waiting_time <= 5.0:
                    if waiting_time <= 4.0:
                        return '__random__'
                    else:
                        if waiting_time <= 4.0:
                            return '__random__'
                        else:
                            return '(switch_light)'
                else:
                    return '(switch_light)'
            else:
                if waiting_time <= 5.0:
                    if waiting_time <= 1.0:
                        if cars_left <= 1.0:
                            return '(wait)'
                        else:
                            return '(switch_light)'
                    else:
                        if cars_left <= 0.0:
                            return '(wait)'
                        else:
                            return '(switch_light)'
                else:
                    return '(switch_light)'
        else:
            if cars_left <= 4.0:
                return '(switch_light)'
            else:
                if waiting_time <= 2.0:
                    if cars_left <= 4.0:
                        return '__random__'
                    else:
                        if cars_left <= 4.0:
                            return '(switch_light)'
                        else:
                            return '__random__'
                else:
                    return '(switch_light)'
