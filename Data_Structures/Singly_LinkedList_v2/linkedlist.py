"""
    LinkedList implementation from:
    https://dbader.org/blog/python-linked-list
"""


class ListNode:
    """
    A node in a singly linkedlist
    """

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return repr(self.data)


class SinglyLinkedList:
    """
    LinkedList implementation
    """

    def __init__(self):
        """
        Create a new linkedlist
        takes O(1) time
        """
        self.head = None

    def __repr__(self):
        """
        returning a string representation of the list
        takes O(n) time
        """
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next()
        return '[' + ', '.join(nodes) + ']'

    def prepend(self, data):
        """
        Insert an element at the beggining of the list
        takes O(1) time
        """
        self.head = ListNode(data=data, next_node=self.head)
