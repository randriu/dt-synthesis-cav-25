######################## Properties ########################
# expected discounted reward: -2.3526163194386696
# expected discounted reward bound: -2.3526163194386696
# value iteration: None
# proven optimal: True
# runtime: 5.485351085662842
######################## Parameters ########################
# depth: 1
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(skipped, player_total, dealer_total):
    if player_total <= 11.0:
        return '(Draw)'
    else:
        return '(Skip)'
