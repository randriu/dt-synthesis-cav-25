######################## Properties ########################
# expected discounted reward: 65.05206545013071
# expected discounted reward bound: 65.5392371091838
# value iteration: None
# proven optimal: False
# runtime: 1200.0461571216583
######################## Parameters ########################
# depth: 4
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, num_tokens_var):
    if q9 <= 0.0:
        if q8 <= 0.0:
            if q10 <= 0.0:
                return 'process1_cmd_0'
            else:
                return 'process10_cmd_9'
        else:
            if q10 <= 0.0:
                if q1 <= 0.0:
                    return 'process8_cmd_7'
                else:
                    return 'process1_cmd_0'
            else:
                if num_tokens_var <= 0.0:
                    return 'process10_cmd_9'
                else:
                    return 'process1_cmd_0'
    else:
        if q7 <= 0.0:
            if q10 <= 0.0:
                return 'process1_cmd_0'
            else:
                if q2 <= 0.0:
                    return 'process3_cmd_2'
                else:
                    return 'process8_cmd_7'
        else:
            if q8 <= 0.0:
                if q3 <= 0.0:
                    return 'process1_cmd_0'
                else:
                    return 'process7_cmd_6'
            else:
                if num_tokens_var <= 0.0:
                    return 'process7_cmd_6'
                else:
                    return '__random__'
