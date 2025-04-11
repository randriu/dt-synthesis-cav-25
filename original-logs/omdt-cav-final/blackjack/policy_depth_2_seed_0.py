######################## Properties ########################
# expected discounted reward: -2.20527150726744
# expected discounted reward bound: -2.20527150726744
# value iteration: None
# proven optimal: True
# runtime: 14.276530981063843
######################## Parameters ########################
# depth: 2
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(skipped, player_total, dealer_total):
    if dealer_total <= 6.0:
        if player_total <= 11.0:
            return '(Draw)'
        else:
            return '(Skip)'
    else:
        if player_total <= 13.0:
            return '(Draw)'
        else:
            return '(Skip)'
