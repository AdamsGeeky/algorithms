#!/usr/bin/python3
import sys
"""
This module solves the birthday chocolate bar from HackerRank the naive way
It is OK since values are assumed to stay small
The one trick for me was to remember in python the last index is always
excluded (last test failed)
"""

def solve(n, s, d, m):
    """
    return the number of subarrays of s of size m summing to d
    subarrays are made of continuous values of s

    Arguments
        n: size of array s
        s: array of ints
        d: sum to match
        m: size of subarray
    """
    if m > n:
        return 0
    subset_sum = sum(s[0:m])
    count = 0
    print(subset_sum)
    for i in range(n - m + 1):
        if subset_sum == d:
            count += 1
        if i + m < n:
            subset_sum = subset_sum - s[i] + s[i + m]
        print(subset_sum)
    return count

if __name__ == "__main__":
    print(solve(5, [1, 2, 1, 3, 2], 3, 2))
    print(solve(1, [4], 4, 1))
    print(solve(1, [5], 4, 1))
    print(solve(4, [4, 0, 0, 0], 4, 4))
    print(solve(5, [4, 1, 0, 4, 1], 5, 2))
    print(solve(4, [0], 4, 4))
    print(solve(4, [4, 0, 0, 0], 0, 4))
    print(solve(4, [4, 0, 0, 0], 4, 0))
    print(solve(19, [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1],
                18, 7))
