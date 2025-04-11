######################## Properties ########################
# expected discounted reward: 65.0345656194577
# expected discounted reward bound: 65.0345656194577
# value iteration: None
# proven optimal: True
# runtime: 504.6178319454193
######################## Parameters ########################
# depth: 1
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, num_tokens_var):
    if q10 <= 0.0:
        return 'process1_cmd_0'
    else:
        return 'process10_cmd_9'
