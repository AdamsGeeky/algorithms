#!/usr/bin/python3
"""
Maximum in sliding window
"""

def max_slide(array, size):
    """
    finds the maximums in sliding windows in array

    Arguments:
        array: any array of int here
        size: size of sliding window

    Return:
        an array with the maximum values
    """
    deque = []
    result = []
    for i in range(len(array)):
        # remove unwanted indexes
        deque = [x for x in deque if (x > (i - size))]
        # max is the last deque element, keep it that way
        while deque and (array[deque[-1]] <= array[i]):
                deque.pop()
        # i could still be in the top k, prepare its place
        while deque and (array[deque[0]] <= array[i]):
                deque.pop(0)
        if not deque:
            deque.append(i)
        else:
            # there is one value larger than i, i is second
            deque.insert(0, i)
        if i >= k - 1:
            result.append(array[deque[-1]])

    return result

if __name__ == "__main__":
    array = [4, 2, 5, 3, 7, 9]
    k = 3
    print(max_slide(array, k))
    arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
    k = 4
    print(max_slide(arr, k))
    arr = [80, 50, 70, 7, 6, 4, 3, 2, 1, 10]
    k = 4
    print(arr)
    print(max_slide(arr, k))
