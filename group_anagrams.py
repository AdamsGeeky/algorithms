#!/usr/bin/python
from collections import defaultdict
"""
extracted from CTCI 6th edition

10.2 Group Anagrams: Write a method to sort an array of strings so that all
 the anagrams are next to each other

Note it is about grouping, not sorting

How to group/compare 2 strings ?
What are anagrams ? Words with the same letters but in different orders.
A way to compare 2 words would be to see if they have the same letters.
So building a comparison function looking for that.

Then, once we have a comparison function we can sort the words. How much does
sorting take: O(nlog(n)).

Actually, since we need grouping, not sorting we can do better using hashing.
Using what we said about the comparison we can build a hash function to put
anagrams in the same buckets
"""

def hash_bucket(s):
    """
    hash a string to another string, the hash
    the has is a string containing all the letters in sorted order

    Arguments:
        s: a string

    Return:
       a hash of the string
    """
    return ''.join(sorted(s))


def group_anagrams(word_list):
    """
    group the anagrams contained in a list of words together

    Arguments:
        word_list: a list of word

    Return:
        a list of words grouped by anagrams
    """
    hash_map = defaultdict(list)
    for word in word_list:
        hash_map[hash_bucket(word)].append(word)
    return [word for values in hash_map.values() for word in values]


if __name__ == "__main__":
    word_list = ["faire", "isocele", "ferai", "acre", "celosie", "intrus",
                 "colisee", "race"]
    print(group_anagrams(word_list))
