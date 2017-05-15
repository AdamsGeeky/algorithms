#!/usr/bin/python3
"""
reverse the vowels in a string
"""

def reverse_vowels(word):
    """
    reverse the vowels in a string

    Arguments:
    word: a string

    Return:
    the partly reversed string
    """
    i = 0
    result = list(word)
    j = len(result) - 1
    vowels = "aeiou"
    while (i < j):
        if result[i] in vowels:
            if result[j] in vowels:
                result[i], result[j] = result[j], result[i]
        i += 1
        j -= 1
    return "".join(result)


if __name__ == "__main__":
    print(reverse_vowels(""))
    print(reverse_vowels("Helbortin"))
