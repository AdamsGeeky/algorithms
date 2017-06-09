#!/usr/bin/python3
"""
This module presents common binary tree functions in python
"""
from collections import deque


class Node:
    """
    Defines an element of a tree

    **Attributes**
        value: value to be held at that node
        parent: parent of the node
        left: left child of the node
        right: right child of the node
    """

    def __init__(self, value):
        """
        Initialize a node object

        Arguments:
            value: value to be held at node

        Return:
           a Node object
        """
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

    def add_parent(self, parent):
        self.parent = parent

    def add_left(self, child):
        """
        add a left child to a node

        Argument:
            child: a node
        """
        self.left = child
        child.parent = self

    def add_right(self, child):
        """
        add a right child to a node

        Argument:
            child: a node
        """
        self.right = child
        child.parent = self

    def level_order_traversal(self):
        """traverse a tree in level order"""
        queue = deque([self])
        while queue:
            n = queue.popleft()
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)
            print(n.value)

    def level_order_print(self):
        """print a tree showing levels (not fancy)"""
        all_levels = []
        all_levels.append([self])
        done = False
        while not done:
            previous_level = all_levels[-1]
            new_level = []
            for node in previous_level:
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            if new_level:
                all_levels.append(new_level)
            else:
                done = True
        print('\n'.join(' '.join([str(node.value) for node in level])
                        for level in all_levels))

    def post_order_rec(self):
        """traverse a tree in a post order with recursion"""
        if self is None:
            return
        if self.left:
            self.left.post_order_rec()
        if self.right:
            self.right.post_order_rec()
        print(self.value)

    def post_order_ite(self):
        """traverse a tree in post order with 2 stacks"""
        stack1 = []
        stack2 = []
        stack1.append(self)
        while stack1:
            n = stack1.pop()
            if n.left:
                stack1.append(n.left)
            if n.right:
                stack1.append(n.right)
            stack2.append(n)
        while stack2:
            print(stack2.pop().value)

    def post_order_ite2(self):
        """traverse a tree in post order with one stack"""
        stack = []
        current = self
        done = False
        while not done:
            while current:
                if current.right:
                    stack.append(current.right)
                stack.append(current)
                current = current.left
            current = stack.pop()
            if stack and stack[-1] == current.right:
                current = stack.pop()
                stack.append(current.parent)
            else:
                print(current.value)
                current = None
                if not stack:
                    done = True

    def pre_order_rec(self):
        """traverse a tree in pre order with recursion"""
        print(self.value)
        if self.left:
            self.left.pre_order_rec()
        if self.right:
            self.right.pre_order_rec()

    def pre_order_ite(self):
        """traverse a tree in pre order with a stack"""
        stack = []
        stack.append(self)
        while stack:
            n = stack.pop()
            print(n.value)
            if n.right:
                stack.append(n.right)
            if n.left:
                stack.append(n.left)

    def in_order_rec(self):
        """traverse a tree in order with recursion"""
        if self.left:
            self.left.in_order_rec()
        print(self.value)
        if self.right:
            self.right.in_order_rec()

    def in_order_ite(self):
        """traverse a tree in order with a stack"""
        stack = []
        stack.append(self)
        current = self
        while stack:
            while current:
                if current.left:
                    stack.append(current.left)
                current = current.left
            current = stack.pop()
            print(current.value)
            current = current.right
            if current:
                stack.append(current)





                
def main():
    root = Node(1)
    root.add_left(Node(2))
    root.add_right(Node(3))
    root.left.add_left(Node(4))
    root.left.add_right(Node(5))
    root.right.add_right(Node(7))
    print("level order")
    root.level_order_traversal()
    root.level_order_print()
    print("post order")
    root.post_order_rec()
    print("--")
    root.post_order_ite2()
    print("pre_order")
    root.pre_order_rec()
    print("--")
    root.pre_order_ite()
    print("in_order")
    root.in_order_rec()
    print("--")
    root.in_order_ite()

    
if __name__ == "__main__":
    main()
    
