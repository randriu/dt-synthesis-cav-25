######################## Properties ########################
# expected discounted reward: 0.09346298277106507
# expected discounted reward bound: 0.09439407263607368
# value iteration: None
# proven optimal: False
# runtime: 1200.2548201084137
######################## Parameters ########################
# depth: 5
# gamma: 0.9999
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(counter, pc1, coin1, pc2, coin2):
    if counter <= 136.0:
        return '__random__'
    else:
        if coin2 <= 1.0:
            if counter <= 136.0:
                return 'done'
            else:
                return '__random__'
        else:
            return '__random__'
