######################## Properties ########################
# expected discounted reward: 212.09654238512434
# expected discounted reward bound: 223.970097134854
# value iteration: None
# proven optimal: False
# runtime: 1200.1214771270752
######################## Parameters ########################
# depth: 3
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(computer_0_running, computer_1_running, computer_2_running, computer_3_running, computer_4_running, computer_5_running, computer_6_running, computer_7_running):
    if computer_5_running <= 0.0:
        if computer_4_running <= 0.0:
            if computer_0_running <= 0.0:
                return '(reboot_computer_4)'
            else:
                return '(reboot_computer_0)'
        else:
            if computer_6_running <= 0.0:
                return '(reboot_computer_0)'
            else:
                return '(reboot_computer_4)'
    else:
        if computer_6_running <= 0.0:
            if computer_0_running <= 0.0:
                return '(reboot_computer_6)'
            else:
                return '(reboot_computer_0)'
        else:
            if computer_1_running <= 0.0:
                return '(reboot_computer_1)'
            else:
                return '(reboot_computer_0)'
