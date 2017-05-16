#!/usr/bin/python3
"""
Find the median of a sorted array that is the union of 2 sorted arrays
"""


def find_median(a1, a2):
    """
    find the median of a1 union a2

    Arguments:
        a1: a sorted array
        a2: a sorted array

    Return:
        median
    """
    print(a1, a2)
    m1 = len(a1) // 2
    m2 = len(a2) // 2
    print("m1: {} m2: {}".format(a1[m1], a2[m2]))
    if len(a1) == 2 and len(a2) == 2:
        return (max(a1[0], a2[0]) + min(a1[1], a2[1])) // 2
    if len(a1) == 1 and len(a2) == 1:
        return (a[m1] + a[m2]) // 2

    if a1[m1] < a2[m2]:
        return find_median(a1[m1:], a2[:m2 + 1])
    else:
        return find_median(a1[:m1 + 1], a2[m2:])


if __name__ == "__main__":
    a1 = [1, 12, 15, 26, 38]
    a2 = [2, 13, 17, 30, 45]
    print(find_median(a1, a2))
    
