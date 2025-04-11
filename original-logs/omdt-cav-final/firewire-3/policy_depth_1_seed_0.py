######################## Properties ########################
# expected discounted reward: -70.52541925218546
# expected discounted reward bound: -70.04494709790646
# value iteration: None
# proven optimal: False
# runtime: 1200.012465953827
######################## Parameters ########################
# depth: 1
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(w12, y1, y2, x1, s1, w21, z1, z2, x2, s2):
    if s2 <= 5.0:
        return 'snd_req21'
    else:
        return 'rec_req21'
