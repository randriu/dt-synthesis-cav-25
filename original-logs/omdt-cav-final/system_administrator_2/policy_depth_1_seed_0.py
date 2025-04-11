######################## Properties ########################
# expected discounted reward: 146.65267307205943
# expected discounted reward bound: 146.65267307205943
# value iteration: None
# proven optimal: True
# runtime: 228.86511516571045
######################## Parameters ########################
# depth: 1
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(computer_0_running, computer_1_running, computer_2_running, computer_3_running, computer_4_running, computer_5_running, computer_6_running, computer_7_running):
    if computer_2_running <= 0.0:
        return '(reboot_computer_2)'
    else:
        return '(reboot_computer_1)'
