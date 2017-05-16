#!/usr/bin/python3
"""
Not algorithms per se but can be nice shortcuts
This is a copy of the set examples in the doc
"""

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
print('orange' in basket)                 # fast membership testing
True
print('crabgrass' in basket)
False

# Demonstrate set operations on unique letters from two words
...
a = set('abracadabra')
b = set('alacazam')
print(a)                                  # unique letters in a
# {'a', 'r', 'b', 'c', 'd'}
print(a - b)                              # letters in a but not in b
# {'r', 'd', 'b'}
print(a | b)                              # letters in either a or b
# {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
print(a & b)                              # letters in both a and b
# {'a', 'c'}
print(a ^ b)                              # letters in a or b but not both
# {'r', 'd', 'b', 'm', 'z', 'l'}
