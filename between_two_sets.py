#!/usr/bin/python3
"""
Find the number of elements between 2 sets
"""
import sys

def pgcd(a, b):
    """GCD of 2 numbers"""
    m = min(a, b)
    M = max(a, b)
    while m:
        M, m = m, M % m
    return M

def pgcd_arr(arr):
    """GCD of an array"""
    p = arr[0]
    for v in arr[1:]:
        p = pgcd(p, v)
    print(p)
    return p

def ppcm_arr(arr):
    """LCM of an array"""
    p = arr[0]
    for v in arr[1:]:
        p = (p * v) / pgcd(p, v)
    print(p)
    return p

def getTotalX(a, b):
    """number of elements between 2 sets"""
    r = pgcd_arr(b) / ppcm_arr(a)
    if r != int(r):
        return 0
    r = int(r)
    count = 0
    for i in range(1, r + 1):
        if r % i == 0:
            count += 1
    return count

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))
total = getTotalX(a, b)
print(total)
