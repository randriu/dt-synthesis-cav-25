######################## Properties ########################
# expected discounted reward: 377.9331340349682
# expected discounted reward bound: 377.9331340349682
# value iteration: None
# proven optimal: True
# runtime: 27.087548971176147
######################## Parameters ########################
# depth: 1
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(computer_0_running, computer_1_running, computer_2_running, computer_3_running, computer_4_running, computer_5_running, computer_6_running):
    if computer_0_running <= 0.0:
        return '(reboot_computer_0)'
    else:
        return '__random__'
