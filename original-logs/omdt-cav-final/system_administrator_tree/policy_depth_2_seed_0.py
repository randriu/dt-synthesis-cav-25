######################## Properties ########################
# expected discounted reward: 433.8170864346918
# expected discounted reward bound: 496.8390391893161
# value iteration: None
# proven optimal: False
# runtime: 1200.003114938736
######################## Parameters ########################
# depth: 2
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(computer_0_running, computer_1_running, computer_2_running, computer_3_running, computer_4_running, computer_5_running, computer_6_running):
    if computer_1_running <= 0.0:
        if computer_2_running <= 0.0:
            return '(reboot_computer_2)'
        else:
            return '(reboot_computer_1)'
    else:
        if computer_0_running <= 0.0:
            return '(reboot_computer_0)'
        else:
            return '__random__'
