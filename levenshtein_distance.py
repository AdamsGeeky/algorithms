#!/usr/bin/python3
"""
I this module I try to implement the Lenshtein or edit distance.
More info on wikipedia
https://en.wikipedia.org/wiki/Levenshtein_distance
"""


def naive_recursive(s1, s2):
    """
    this approach should not be used as it requires to compute things multiple
    times

    Arguments:
        s1: a string
        s2: a string

    Return:
        number of edits to make to go from on string to the other
    """
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)
    if s1[0] == s2[0]:
        return naive_recursive(s1[1:], s2[1:])
    return 1 + min(naive_recursive(s1, s2[1:]),  # insert into s1 to match s2
                   naive_recursive(s1[1:], s2),  # remove from ...
                   naive_recursive(s1[1:], s2[1:]))  # replace


def dyn(s1, s2):
    """
    use memoisation, store previous calculations in an array

    Arguments:
        s1: a string
        s2: a string

    Return:
        number of edits to make to go from on string to the other
    """
    m = len(s1)
    n = len(s2)
    changes = []
    for i in range(m + 1):
        changes.append([0] * (n + 1))
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                changes[i][j] = j
            elif j == 0:
                changes[i][j] = i
            elif s1[i-1] == s2[j-1]:
                changes[i][j] = changes[i-1][j-1]
            else:
                changes[i][j] = 1 + min(changes[i-1][j],
                                        changes[i][j-1],
                                        changes[i-1][j-1])
    return changes[m][n]


def less_than_2(s1, s2):
    """
    checks if the number of edit/remove/replace between 2 strings is less than
    2

    Arguments:
        s1: a string
        s2: a string

    Return:
        number of edits to make to go from on string to the other
    """
    l1 = len(s1)
    l2 = len(s2)
    if l1 > l2 + 1:
        return False
    if l2 > l1 + 1: False
    big_s = s1 if len(s1) >= len(s2) else s2
    small_s = s2 if big_s == l1 else s1
    i = 0
    j = 0
    count = 0
    while i < len(small_s):
        if big_s[j] != small_s[j]:
            count += 1
            if count > 1:
                return False
            if l1 == l2:
                i += 1 # no insert possible
        else:
            i += 1
        j += 1
    return True


if __name__ == "__main__":
    s1 = "kitten"
    s2 = "kitten"
    print(naive_recursive(s1, s2))
    print(less_than_2(s1, s2))
    print(dyn(s1, s2))
    s2 = "kittens"
    print(naive_recursive(s1, s2))
    print(less_than_2(s1, s2))
    print(dyn(s1, s2))
    s2 = "sitting"
    print(naive_recursive(s1, s2))
    print(less_than_2(s1, s2))
    print(dyn(s1, s2))
    s1 = "sunday"
    s2 = "saturday"
    print(naive_recursive(s1, s2))
    print(less_than_2(s1, s2))
    print(dyn(s1, s2))
