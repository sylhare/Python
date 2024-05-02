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

    def height(self, node):
        if node is None:
            return -1

        return 1 + max(self.height(node.left), self.height(node.right))


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


def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.value, end=" ")
        in_order(node.right)


def pre_order(node):
    if node is not None:
        print(node.value, end=" ")
        pre_order(node.left)
        pre_order(node.right)


def post_order(node):
    if node is not None:
        post_order(node.left)
        post_order(node.right)
        print(node.value, end=" ")


def level_order(node):
    queue = [node]
    while len(queue):
        current = queue.pop(0)
        print(current.value, end=" ")
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


def height(node, right=0, left=0):
    if node.left:
        left = height(node.left) + 1
    if node.right:
        right = height(node.right) + 1

    return max(left, right)


def top_view_recursive(root):
    result = top_nodes(root)
    for i in sorted(result.keys()):
        print(result[i]["info"], end=" ")


def top_nodes(root, x=0, y=0, result={}):
    if result.get(x) is None or result[x]["y"] > y:
        result[x] = {"y": y, "info": root.value}
    if root.left:
        result = top_nodes(root.left, x - 1, y + 1, result)
    if root.right:
        result = top_nodes(root.right, x + 1, y + 1, result)
    return result


def top_view(root, y=0, result={}):
    queue = [(root, 0)]

    for node, x in queue:
        if result.get(x) is None or result[x][1] > y:
            result[x] = (node.value, y)
        if node.left:
            queue.extend([(node.left, x - 1)])
        if node.right:
            queue.extend([(node.right, x + 1)])
        y += 1

    [print(result[i][0], end=" ") for i in sorted(result.keys())]


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
    in_order(deserialize_tree("1 2 5 3 4 6").root)
    print()
