######################## Properties ########################
# expected discounted reward: -2.352615118845449
# expected discounted reward bound: -2.173208593159659
# value iteration: None
# proven optimal: False
# runtime: 1200.0259881019592
######################## Parameters ########################
# depth: 7
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(skipped, player_total, dealer_total):
    if player_total <= 5.0:
        if player_total <= 0.0:
            if dealer_total <= 0.0:
                if dealer_total <= 10.0:
                    if dealer_total <= 3.0:
                        return '__random__'
                    else:
                        return '(Skip)'
                else:
                    if dealer_total <= 21.0:
                        return '(Skip)'
                    else:
                        return '(Draw)'
            else:
                if dealer_total <= 22.0:
                    return '(Skip)'
                else:
                    if dealer_total <= 22.0:
                        return '(Draw)'
                    else:
                        return '(Skip)'
        else:
            if skipped <= 0.0:
                if player_total <= 6.0:
                    if dealer_total <= 22.0:
                        return '(Draw)'
                    else:
                        return '(Skip)'
                else:
                    return '__random__'
            else:
                if dealer_total <= 2.0:
                    return '(Skip)'
                else:
                    if dealer_total <= 21.0:
                        return '__random__'
                    else:
                        return '(Draw)'
    else:
        if dealer_total <= 2.0:
            if player_total <= 13.0:
                if player_total <= 5.0:
                    return '(Skip)'
                else:
                    if player_total <= 11.0:
                        return '(Draw)'
                    else:
                        return '(Skip)'
            else:
                if player_total <= 21.0:
                    return '(Skip)'
                else:
                    return '(Draw)'
        else:
            if player_total <= 0.0:
                if dealer_total <= 22.0:
                    return '(Draw)'
                else:
                    return '(Skip)'
            else:
                if player_total <= 9.0:
                    if skipped <= 0.0:
                        return '(Draw)'
                    else:
                        return '__random__'
                else:
                    if player_total <= 11.0:
                        return '(Draw)'
                    else:
                        if skipped <= 0.0:
                            return '(Skip)'
                        else:
                            return '(Draw)'
