######################## Properties ########################
# expected discounted reward: -2.1732085931596337
# expected discounted reward bound: -2.1732085931596337
# value iteration: None
# proven optimal: True
# runtime: 143.5600118637085
######################## Parameters ########################
# depth: 3
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(skipped, player_total, dealer_total):
    if dealer_total <= 9.0:
        if dealer_total <= 6.0:
            if player_total <= 11.0:
                return '(Draw)'
            else:
                return '(Skip)'
        else:
            if player_total <= 14.0:
                return '(Draw)'
            else:
                return '(Skip)'
    else:
        if dealer_total <= 10.0:
            if player_total <= 13.0:
                return '(Draw)'
            else:
                return '(Skip)'
        else:
            if player_total <= 11.0:
                return '(Draw)'
            else:
                return '(Skip)'
