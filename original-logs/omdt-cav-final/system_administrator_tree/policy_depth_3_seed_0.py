######################## Properties ########################
# expected discounted reward: 467.7392010606897
# expected discounted reward bound: 557.7247113347798
# value iteration: None
# proven optimal: False
# runtime: 1200.0044808387756
######################## Parameters ########################
# depth: 3
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(computer_0_running, computer_1_running, computer_2_running, computer_3_running, computer_4_running, computer_5_running, computer_6_running):
    if computer_2_running <= 0.0:
        if computer_1_running <= 0.0:
            if computer_0_running <= 0.0:
                return '(reboot_computer_0)'
            else:
                return '(reboot_computer_1)'
        else:
            if computer_0_running <= 0.0:
                return '(reboot_computer_0)'
            else:
                return '(reboot_computer_2)'
    else:
        if computer_4_running <= 0.0:
            if computer_3_running <= 0.0:
                return '(reboot_computer_3)'
            else:
                return '(reboot_computer_4)'
        else:
            if computer_1_running <= 0.0:
                return '(reboot_computer_1)'
            else:
                return '__random__'
