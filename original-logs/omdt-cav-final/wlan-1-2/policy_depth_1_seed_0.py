######################## Properties ########################
# expected discounted reward: 0.039549000597767725
# expected discounted reward bound: 0.10827098374805666
# value iteration: None
# proven optimal: False
# runtime: 1200.0203728675842
######################## Parameters ########################
# depth: 1
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(col, c1, c2, x1, s1, slot1, backoff1, bc1, x2, s2, slot2, backoff2, bc2):
    if x1 <= 5.0:
        return 'time'
    else:
        return 'finish2'
