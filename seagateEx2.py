"""
Ex. 2 - Max subarray

will elaborate tomorrow
"""

# ======================================================================================================================
def max_subarray(nums_array: list):
    """
    Using "Maximum subarray problem" with dynamic programming solution
    :param nums_array: a list of nums_array
    :return: Tuple, the indexes of the maximum subarray (e.g for [0, 10, 20, -647, 10, 4, 20] will return (4, 7)
    """
    best_sum = 0  # or: float('-inf')
    current_start = best_start = best_end = 0  # or: None
    current_sum = 0
    for current_end, x in enumerate(nums_array):
        if current_sum <= 0:
            current_start = current_end
            current_sum = x
        else:
            current_sum += x

        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = current_end + 1
    return best_start, best_end


# ======================================================================================================================
if __name__ == '__main__':
    a = [-2, -3, 4, -1, -2, 1, 5, -3]
    b = [0, 10, 20, -647, 10, 4, 20]
    c = [1 for _ in range(7)]
    print(max_subarray(a))
    print(max_subarray(b))
    print(max_subarray(c))
