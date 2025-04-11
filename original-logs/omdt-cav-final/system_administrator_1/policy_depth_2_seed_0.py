######################## Properties ########################
# expected discounted reward: 209.9507201355646
# expected discounted reward bound: 209.9507201355646
# value iteration: None
# proven optimal: True
# runtime: 884.8719751834869
######################## Parameters ########################
# depth: 2
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(computer_0_running, computer_1_running, computer_2_running, computer_3_running, computer_4_running, computer_5_running, computer_6_running, computer_7_running):
    if computer_5_running <= 0.0:
        if computer_6_running <= 0.0:
            return '(reboot_computer_0)'
        else:
            return '(reboot_computer_4)'
    else:
        if computer_5_running <= 0.0:
            return '(reboot_computer_2)'
        else:
            return '(reboot_computer_0)'
