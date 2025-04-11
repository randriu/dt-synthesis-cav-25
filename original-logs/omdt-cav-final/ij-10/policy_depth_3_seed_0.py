######################## Properties ########################
# expected discounted reward: 65.03315832411965
# expected discounted reward bound: 65.5392371091921
# value iteration: None
# proven optimal: False
# runtime: 1200.035169839859
######################## Parameters ########################
# depth: 3
# gamma: 0.99
# max_iter: 1000
# delta: 1e-10
# seed: 0
############################################################
def act(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, num_tokens_var):
    if q9 <= 0.0:
        if q8 <= 0.0:
            return 'process1_cmd_0'
        else:
            return 'process3_cmd_2'
    else:
        if q7 <= 0.0:
            if q5 <= 0.0:
                return 'process4_cmd_3'
            else:
                return 'process5_cmd_4'
        else:
            return 'process2_cmd_1'
