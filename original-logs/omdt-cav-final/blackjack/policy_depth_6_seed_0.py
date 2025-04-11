######################## Properties ########################
# expected discounted reward: -2.1732085931596217
# expected discounted reward bound: -2.1732085931596217
# value iteration: None
# proven optimal: True
# runtime: 1106.6389617919922
######################## Parameters ########################
# depth: 6
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(skipped, player_total, dealer_total):
    if skipped <= 0.0:
        if player_total <= 13.0:
            if dealer_total <= 22.0:
                if dealer_total <= 10.0:
                    if dealer_total <= 6.0:
                        if player_total <= 11.0:
                            return '(Draw)'
                        else:
                            return '(Skip)'
                    else:
                        return '(Draw)'
                else:
                    if player_total <= 11.0:
                        if dealer_total <= 19.0:
                            return '(Draw)'
                        else:
                            return '(Skip)'
                    else:
                        return '(Skip)'
            else:
                return '(Skip)'
        else:
            if player_total <= 17.0:
                if dealer_total <= 9.0:
                    if player_total <= 14.0:
                        if dealer_total <= 6.0:
                            return '(Skip)'
                        else:
                            return '(Draw)'
                    else:
                        return '(Skip)'
                else:
                    return '(Skip)'
            else:
                if player_total <= 13.0:
                    if dealer_total <= 22.0:
                        return '__random__'
                    else:
                        return '(Skip)'
                else:
                    return '(Skip)'
    else:
        if dealer_total <= 21.0:
            return '(Skip)'
        else:
            if player_total <= 11.0:
                if dealer_total <= 22.0:
                    return '(Skip)'
                else:
                    if dealer_total <= 22.0:
                        return '__random__'
                    else:
                        return '(Skip)'
            else:
                if dealer_total <= 22.0:
                    if player_total <= 11.0:
                        return '(Skip)'
                    else:
                        if player_total <= 14.0:
                            return '(Draw)'
                        else:
                            return '__random__'
                else:
                    return '(Skip)'
