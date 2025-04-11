######################## Properties ########################
# expected discounted reward: 214.94674323033507
# expected discounted reward bound: 223.97009716133113
# value iteration: None
# proven optimal: False
# runtime: 1200.0449998378754
######################## Parameters ########################
# depth: 7
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(computer_0_running, computer_1_running, computer_2_running, computer_3_running, computer_4_running, computer_5_running, computer_6_running, computer_7_running):
    if computer_6_running <= 0.0:
        if computer_0_running <= 0.0:
            if computer_5_running <= 0.0:
                return '(reboot_computer_0)'
            else:
                if computer_5_running <= 0.0:
                    return '(reboot_computer_0)'
                else:
                    if computer_4_running <= 0.0:
                        return '(reboot_computer_0)'
                    else:
                        return '(reboot_computer_6)'
        else:
            if computer_4_running <= 0.0:
                if computer_1_running <= 0.0:
                    if computer_2_running <= 0.0:
                        return '(reboot_computer_0)'
                    else:
                        return '(reboot_computer_1)'
                else:
                    return '(reboot_computer_0)'
            else:
                if computer_2_running <= 0.0:
                    return '(reboot_computer_0)'
                else:
                    if computer_5_running <= 0.0:
                        if computer_7_running <= 1.0:
                            if computer_0_running <= 0.0:
                                return '(reboot_computer_5)'
                            else:
                                return '(reboot_computer_0)'
                        else:
                            return '(reboot_computer_0)'
                    else:
                        if computer_5_running <= 0.0:
                            return '(reboot_computer_0)'
                        else:
                            return '(reboot_computer_6)'
    else:
        if computer_3_running <= 0.0:
            if computer_5_running <= 0.0:
                if computer_1_running <= 0.0:
                    if computer_6_running <= 0.0:
                        return '(reboot_computer_0)'
                    else:
                        return '(reboot_computer_4)'
                else:
                    if computer_0_running <= 0.0:
                        if computer_4_running <= 0.0:
                            return '(reboot_computer_0)'
                        else:
                            return '(reboot_computer_4)'
                    else:
                        if computer_2_running <= 0.0:
                            return '(reboot_computer_0)'
                        else:
                            if computer_2_running <= 0.0:
                                return '(reboot_computer_0)'
                            else:
                                return '(reboot_computer_4)'
            else:
                if computer_5_running <= 0.0:
                    return '(reboot_computer_0)'
                else:
                    if computer_7_running <= 0.0:
                        if computer_1_running <= 0.0:
                            return '(reboot_computer_5)'
                        else:
                            return '(reboot_computer_7)'
                    else:
                        if computer_1_running <= 0.0:
                            if computer_0_running <= 0.0:
                                return '(reboot_computer_2)'
                            else:
                                return '(reboot_computer_1)'
                        else:
                            return '(reboot_computer_0)'
        else:
            if computer_7_running <= 1.0:
                if computer_4_running <= 0.0:
                    if computer_7_running <= 0.0:
                        if computer_5_running <= 0.0:
                            return '(reboot_computer_1)'
                        else:
                            return '(reboot_computer_7)'
                    else:
                        if computer_7_running <= 0.0:
                            return '(reboot_computer_0)'
                        else:
                            if computer_1_running <= 0.0:
                                return '(reboot_computer_0)'
                            else:
                                return '__random__'
                else:
                    if computer_6_running <= 0.0:
                        if computer_1_running <= 0.0:
                            return '__random__'
                        else:
                            return '(reboot_computer_4)'
                    else:
                        if computer_5_running <= 0.0:
                            return '(reboot_computer_4)'
                        else:
                            if computer_2_running <= 0.0:
                                return '(reboot_computer_2)'
                            else:
                                return '(reboot_computer_0)'
            else:
                return '(reboot_computer_0)'
