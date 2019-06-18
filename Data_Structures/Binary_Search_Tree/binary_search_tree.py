"""
Binary Tree implementaion
uses node
"""
from node import Node


class BinarySearchTree():
    """ this is an implementation of binary search tree"""

    def __init__(self):
        self.root = None

    def insert(self, data):
        """ insert data to tree """
        if self.root:
            # if root already have data
            # call insert function of that node
            return self.root.insert(data)
        else:
            # create new node as root
            self.root = Node(data)
            return True

    def find(self, data):
        """ find data within the tree """
        if self.root:
            # if root have data, call node's find method
            self.root.find(data)
        else:
            # data not found
            return False

    def pre_order(self):
        """ wrapper for preorder function of the node """
        if self.root is not None:
            print("pre order traversal")
            self.root.pre_order()

    def post_order(self):
        """ wrapper for post order function of the node """
        if self.root is not None:
            print("post order traversal")
            self.root.post_order()

    def in_order(self):
        """ wrapper for in order function of the node """
        if self.root is not None:
            print("in order traversal")
            self.root.in_order()

    def level_order(self):
        """ wrapper for level order function of the node """
        if self.root is not None:
            print("level order traversal")
            self.root.level_order()

    def get_height(self):
        """ wrapper for get height function of the node """
        if self.root:
            return self.root.get_height()
        else:
            return 0

    def get_size(self):
        """ wrapper for get size function of the node """
        if self.root:
            return self.root.get_size()
        else:
            return 0
