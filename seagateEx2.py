"""

"""
# ======================================================================================================================
def calc_ladder_steps(curr_step):
    """
    Ex. 1 a
    Recursive function to calculate possible ways to climb on a n steps ladder (when only 1 or 2 steps
    are allowed on each climbing attempt)
    :param curr_step: the current ladder size
    :return: possible climbing options for "curr_steps"
    """
    if curr_step == 1:
        return 1
    elif curr_step == 2:
        return 2
    return calc_ladder_steps(curr_step - 1) + calc_ladder_steps(curr_step - 2)


# ======================================================================================================================
def calc_ladder_steps_with_dictionary_values(curr_step, steps_dict):
    """
    This function is the improvement for ex 1 a.
    When running multiple times, a kind of database is necessary to save some computations.
    So, we create a dict, with the computed times and check if the value reached in the recursion is in the dict.
    If so, we return it's value, instead of running the recursive computations again.
    :param curr_step:
    :param steps_dict
    :return:
    """
    if curr_step == 1:
        return 1
    elif curr_step == 2:
        return 2
    elif curr_step in steps_dict:
        return steps_dict[curr_step]
    return calc_ladder_steps_with_dictionary_values(curr_step - 1, steps_dict) + \
           calc_ladder_steps_with_dictionary_values(curr_step - 2, steps_dict)


# ======================================================================================================================
# 1 1 2 3 5 8 13 21 34 55 89
# 0 1 2 3 4 5 6  7  8  9  10
if __name__ == '__main__':
    print(calc_ladder_steps(8))
    steps_dict = {1: "1",
                  2: "2",
                  3: "3",
                  4: "5",
                  5: "8"}
    steps_dict[8] = calc_ladder_steps_with_dictionary_values(8, steps_dict)
    print(steps_dict[8])
