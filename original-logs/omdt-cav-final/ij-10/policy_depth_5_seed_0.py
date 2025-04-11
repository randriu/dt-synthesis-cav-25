######################## Properties ########################
# expected discounted reward: 65.03449007798822
# expected discounted reward bound: 65.5392371091957
# value iteration: None
# proven optimal: False
# runtime: 1200.0189790725708
######################## Parameters ########################
# depth: 5
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, num_tokens_var):
    if num_tokens_var <= 0.0:
        if q2 <= 0.0:
            return 'process1_cmd_0'
        else:
            return 'process2_cmd_1'
    else:
        return 'process1_cmd_0'
