######################## Properties ########################
# expected discounted reward: 65.03071812464032
# expected discounted reward bound: 65.5392371091794
# value iteration: None
# proven optimal: False
# runtime: 1200.1804010868073
######################## Parameters ########################
# depth: 8
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, num_tokens_var):
    if num_tokens_var <= 0.0:
        if q5 <= 0.0:
            return 'process1_cmd_0'
        else:
            if q2 <= 0.0:
                return 'process3_cmd_2'
            else:
                return 'process2_cmd_1'
    else:
        if num_tokens_var <= 0.0:
            if q6 <= 0.0:
                return 'process2_cmd_1'
            else:
                return 'process10_cmd_9'
        else:
            return 'process1_cmd_0'
