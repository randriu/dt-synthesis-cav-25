######################## Properties ########################
# expected discounted reward: 65.04118820254483
# expected discounted reward bound: 65.53923710918387
# value iteration: None
# proven optimal: False
# runtime: 1200.0058641433716
######################## Parameters ########################
# depth: 2
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, num_tokens_var):
    if q4 <= 0.0:
        if q10 <= 0.0:
            return 'process1_cmd_0'
        else:
            return 'process10_cmd_9'
    else:
        if q10 <= 0.0:
            return 'process9_cmd_8'
        else:
            return 'process4_cmd_3'
