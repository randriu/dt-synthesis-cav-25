######################## Properties ########################
# expected discounted reward: 0.09339330092319562
# expected discounted reward bound: 392.0392039203927
# value iteration: None
# proven optimal: False
# runtime: 1201.1798179149628
######################## Parameters ########################
# depth: 7
# gamma: 0.9999
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(counter, pc1, coin1, pc2, coin2):
    if coin2 <= 1.0:
        return 'process2_cmd_9'
    else:
        return '__random__'
