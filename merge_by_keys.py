#!/usr/bin/python3
"""
merge 2 dictionaries by keys
in case of equal keys, take dictionary 1 value
"""

def merge_key(dict1, dict2):
    """
    merge the dictionaries by keys

    Arguments:
       dict1: a dictionary
       dict2: a dictionary

    Returns:
       the merged dictionary
    """
    # use a shallow copy otherwise import copy use deepcopy
    merged = dict2.copy()
    merged.update(dict1)
    return (merged)

if __name__ == "__main__":
    dict1 = {'one': 1, 'two': 2}
    dict2 = {'two': "deux", 'three': "trois"}
    print(merge_key(dict1, dict2))
