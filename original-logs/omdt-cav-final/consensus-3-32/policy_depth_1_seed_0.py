######################## Properties ########################
# expected discounted reward: 0.09346298277106507
# expected discounted reward bound: 0.09439407263400879
# value iteration: None
# proven optimal: False
# runtime: 1200.022920846939
######################## Parameters ########################
# depth: 1
# gamma: 0.9999
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(counter, pc1, coin1, pc2, coin2):
    if coin2 <= 1.0:
        return 'done'
    else:
        return '__random__'
