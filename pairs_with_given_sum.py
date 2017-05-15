#!/usr/bin/python3
"""
pairs with given sum
consider 2 cases: the given array is sorted or non sorted
"""

def matching_pairs(array, target):
    """
    find pairs in array which sum matches target

    Arguments:
        array: a sorted array
        target: a number
    """
    l = len(array) - 1
    i = 0
    j = l
    while i < l and j > 0:
        s = array[i] + array[j]
        if s < target:
            i += 1
        elif s > target:
            j -= 1
        else:
            return True
    return False

def matching_unsorted(array, target):
    """
    find pairs in array which sum matches target

    Arguments:
        array: a sorted array
        target: a number
    """
    already_seen = []

    for value in array:
        complement = target - value
        if complement in already_seen:
            return True
        already_seen.append(value)
    return False


if __name__ == "__main__":
    array = [1, 2, 3, 9]
    target = 8

    print(matching_pairs(array, target))
    array = [1, 2, 4, 4]
    print(matching_pairs(array, target))

    array = [9, 2, 1, 3]
    print(matching_unsorted(array, target))
    array = [4, 2, 1, 4]
    print(matching_unsorted(array, target))
