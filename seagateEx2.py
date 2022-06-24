"""
Ex. 2 - Max subarray

Given an list of integers of the size of N,
you need to return (start_index, end_index) to designate the subarray with the highest sum.

Notes:
Please provide a naïve solution
There’s a solution that solves the problem using a single iteration – please try to provide it as well.

"""


# ======================================================================================================================
def max_subarray(nums_array: list):
    """
    Using "Maximum subarray problem" with dynamic programming solution
    To return a python slicing tuple for the list, add (1) to the return statement (as '''end + 1''')
    :param nums_array: a list of nums_array
    :return: Tuple, the indexes of the maximum subarray (e.g for [0, 10, 20, -647, 10, 4, 20] will return (4, 6)
    """
    curr_max = final_max_sum = nums_array[0]
    start = end = max_start = 0

    for i in range(0, len(nums_array)):

        curr_max += nums_array[i]

        if final_max_sum < curr_max:
            final_max_sum = curr_max
            max_start = start
            end = i

        if curr_max < 0:
            curr_max = 0
            start = i + 1
    return max_start, end


# ======================================================================================================================
if __name__ == '__main__':
    # test cases fot you to use
    a = [-2, -3, 4, -1, -2, 1, 5, -3]  # 2, 6
    b = [0, 10, 20, -647, 10, 4, 20]
    c = [1 for _ in range(7)]
    d = [-10, -9, -8, -7, -6, -12, -9]
    print(max_subarray(a))
    print(max_subarray(b))
    print(max_subarray(c))
    print(max_subarray(d))

