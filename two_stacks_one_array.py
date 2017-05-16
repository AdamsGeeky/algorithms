#!/usr/bin/python3
"""
Implement 2 stacks in one array
"""

class TwoStacks:
    """
    class 2 stacks

    **attribute**
        array: array for 2 stacks
        size: size of array
        __s1_index: index of the first stack (push and pop)
        __s2_index: index of the 2nd stack (push and pop)
    """
    def __init__(self, size):
        # no error checking
        self.array = size * [None]
        self.size = size
        self.__s1_index = 0
        self.__s2_index = size - 1

    def is_full(self):
        """check if the array is full"""
        return (self.__s1_index > self.__s2_index)

    def push1(self, value):
        """push value in first stack"""
        if self.is_full():
            print("Array is full")
            return
        self.array[self.__s1_index] = value
        self.__s1_index += 1

    def pop1(self):
        """pop value in first stack"""
        if self.__s1_index > 0:
            self.__s1_index -= 1
            return self.array[self.__s1_index]
        print("stack 1 is empty")

    def push2(self, value):
        """push value in first stack"""
        if self.is_full():
            print("Array is full")
            return
        self.array[self.__s2_index] = value
        self.__s2_index -= 1

    def pop2(self):
        """pop value in first stack"""
        if self.__s2_index < self.size - 1:
            self.__s2_index += 1
            return self.array[self.__s2_index]
        print("stack 2 is empty")


if __name__ == "__main__":
    TS = TwoStacks(4)
    TS.push1(1)
    print(TS.array)
    TS.push2(2)
    print(TS.array)
    TS.push1(3)
    print(TS.array)
    TS.push2(4)
    print(TS.array)
    TS.push1(5)
    print(TS.array)
    print("pop1")
    print(TS.pop1())
    print("pop2")
    print(TS.pop2())
    print("pop1")
    print(TS.pop1())
    print("pop2")
    print(TS.pop2())
    print("pop1")
    TS.pop1()
    print("pop2")
    TS.pop2()
