######################## Properties ########################
# expected discounted reward: -2.173208593159626
# expected discounted reward bound: -2.173208593159626
# value iteration: None
# proven optimal: True
# runtime: 168.1303310394287
######################## Parameters ########################
# depth: 4
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(skipped, player_total, dealer_total):
    if player_total <= 13.0:
        if dealer_total <= 8.0:
            if player_total <= 11.0:
                return '(Draw)'
            else:
                if dealer_total <= 6.0:
                    return '(Skip)'
                else:
                    return '(Draw)'
        else:
            if dealer_total <= 10.0:
                if skipped <= 0.0:
                    return '(Draw)'
                else:
                    return '__random__'
            else:
                if player_total <= 11.0:
                    return '(Draw)'
                else:
                    return '(Skip)'
    else:
        if dealer_total <= 9.0:
            if player_total <= 14.0:
                if dealer_total <= 6.0:
                    return '(Skip)'
                else:
                    return '(Draw)'
            else:
                if dealer_total <= 0.0:
                    return '(Draw)'
                else:
                    return '(Skip)'
        else:
            if dealer_total <= 17.0:
                return '(Skip)'
            else:
                if dealer_total <= 18.0:
                    return '(Draw)'
                else:
                    return '(Skip)'
