######################## Properties ########################
# expected discounted reward: 65.06718981603255
# expected discounted reward bound: 65.53923710918278
# value iteration: None
# proven optimal: False
# runtime: 1201.0070490837097
######################## Parameters ########################
# depth: 7
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, num_tokens_var):
    if num_tokens_var <= 0.0:
        if q4 <= 0.0:
            return 'process1_cmd_0'
        else:
            if q10 <= 0.0:
                if q1 <= 0.0:
                    return 'process2_cmd_1'
                else:
                    return 'process1_cmd_0'
            else:
                return 'process10_cmd_9'
    else:
        return 'process1_cmd_0'
