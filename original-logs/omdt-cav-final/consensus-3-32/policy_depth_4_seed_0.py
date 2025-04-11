######################## Properties ########################
# expected discounted reward: 0.09360031891449558
# expected discounted reward bound: 0.09439407259555252
# value iteration: None
# proven optimal: False
# runtime: 1200.1338591575623
######################## Parameters ########################
# depth: 4
# gamma: 0.9999
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(counter, pc1, coin1, pc2, coin2):
    if coin2 <= 1.0:
        if coin2 <= 0.0:
            return 'process1_cmd_1'
        else:
            return '__random__'
    else:
        return '__random__'
