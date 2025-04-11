######################## Properties ########################
# expected discounted reward: 0.09346668164758024
# expected discounted reward bound: 0.09439407263103744
# value iteration: None
# proven optimal: False
# runtime: 1200.2244038581848
######################## Parameters ########################
# depth: 2
# gamma: 0.9999
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(counter, pc1, coin1, pc2, coin2):
    if counter <= 191.0:
        if counter <= 189.0:
            return '__random__'
        else:
            return 'process1_cmd_0'
    else:
        if counter <= 194.0:
            return 'done'
        else:
            return 'process2_cmd_8'
