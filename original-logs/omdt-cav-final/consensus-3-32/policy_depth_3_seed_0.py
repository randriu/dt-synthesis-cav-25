######################## Properties ########################
# expected discounted reward: 0.09362519329933254
# expected discounted reward bound: 0.09439405825855855
# value iteration: None
# proven optimal: False
# runtime: 1200.0648200511932
######################## Parameters ########################
# depth: 3
# gamma: 0.9999
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(counter, pc1, coin1, pc2, coin2):
    if counter <= 194.0:
        if counter <= 193.0:
            return 'process2_cmd_8'
        else:
            if coin2 <= 0.0:
                return 'process2_cmd_8'
            else:
                return '__random__'
    else:
        if counter <= 194.0:
            return '__random__'
        else:
            if counter <= 195.0:
                return 'process1_cmd_1'
            else:
                return '__random__'
