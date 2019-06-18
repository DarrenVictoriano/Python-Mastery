"""
My own implementation of a Queue
Helper for level order traversal
"""


class Queue():
    """ Queue class """

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """ add item on index 0 """
        self.items.insert(0, item)

    def dequeue(self):
        """ pop item """
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        """ check if list is empty """
        return len(self.items) == 0

    def peek(self):
        """ peek top of the queue """
        if not self.is_empty():
            return self.items[-1].data

    def __len__(self):
        """ overwrite len function of the list """
        return self.size()

    def size(self):
        """ return length of the list """
        return len(self.items)
