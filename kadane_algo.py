#!/usr/bin/python3
"""
Kadane's algorithm for maximum subarray problem
"""


def max_subarray(array):
    """
    returns the maximum subarray

    Arguments:
       array: an array of int
    """
    # check if there is more than 1 positive value
    value = 0
    positives = 0
    for i in range(1, len(array)):
        if array[i] > 0:
            positives += 1
        if positives > 1:
            break
        if array[i] > array[value]:
            value = i
    if positives <= 1:
        return value, value

    min_index_far = 1
    max_index_far = 1
    min_index_here = 1
    max_index_here = 1
    max_so_far = array[0]
    max_ending_here = array[0]
    for i in range(1, len(array)):
        if array[i] >= (max_ending_here + array[i]):
            min_index_here = i
            max_index_here = i
            max_ending_here = array[i]
        else:
            max_index_here = i
            max_ending_here += array[i]
        if max_ending_here >= max_so_far:
            min_index_far = min_index_here
            max_index_far = max_index_here
            max_so_far = max_ending_here
    return (min_index_far, max_index_far)


if __name__ == "__main__":
    a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
    print(a)
    print(max_subarray(a))
    a = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(a)
    print(max_subarray(a))
