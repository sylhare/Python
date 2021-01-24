#!/usr/bin/python3.7
"""
Ordered binary tree (aka binary search tree):
 - each left child node is less than its parent node's value
 - each right child node is greater than its parent node's value.
 - No duplicate values

"""


class Node:
    """
    Node is defined as
    self.left (the left child of the node)
    self.right (the right child of the node)
    self.value (the value of the node)
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            # First one is Root
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.value:
                    # New nodes with lower values than current are on the left
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.value:
                    # New nodes with higher value than current are on the right
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    # Can't have two nodes with same value
                    break


def inOrder(node):
    if node is not None:
        inOrder(node.left)
        print(node.value, end=" ")
        inOrder(node.right)


def preOrder(node):
    if node is not None:
        print(node.value, end=" ")
        inOrder(node.left)
        inOrder(node.right)


def postOrder(node):
    if node is not None:
        inOrder(node.left)
        inOrder(node.right)
        print(node.value, end=" ")


def levelOrder(root):
    queue = [root]
    while len(queue):
        current = queue.pop(0)
        print(current.info, end=" ")
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


def deserialize_tree(serialized_tree):
    print(serialized_tree, end="\t\t-> ")
    tree = BinarySearchTree()

    arr = list(map(int, serialized_tree.split()))

    for i in range(len(arr)):
        tree.create(arr[i])

    return tree


if __name__ == "__main__":
    import sys

    print(sys.version)
    inOrder(deserialize_tree("1 2 5 3 4 6").root)
    print()
    inOrder(deserialize_tree("2 1 3 4 5").root)
    print()
    inOrder(deserialize_tree("6 2 5 3 8 1 9").root)
    print()
    inOrder(deserialize_tree("5 1 3 6 2 4").root)
    print()
    inOrder(deserialize_tree("5 1 6 2 4 3").root)
    print()
    inOrder(deserialize_tree("33 21 20 35 34 54").root)
    print()
    inOrder(deserialize_tree("12 6 6 5 4 2 6 2 12 3").root)
    print()
