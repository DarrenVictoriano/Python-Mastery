"""
This is a simple singly linked list implementation from
the book Elements of Programming Interview in Python.
"""


class ListNode:
    """
    simple singly list
    self.data = data
    self.next = ListNode()
    """

    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

    def make_node(self, data: int) -> 'ListNode':
        """ make new node out of data"""
        return ListNode(data)

    def search_list(self, list_node: 'ListNode', key: int) -> 'ListNode':
        """
        list_node - ListNode
        key - Item to search for
        """
        while list_node and list_node.data != key:
            list_node = list_node.next

        # if key was not present in the list, L will have become null
        return list_node

    def insert(self, data):
        new_node = self.make_node(data)
        new_node.next = self.next
        self.next = new_node

    def insert_after(self, node: 'ListNode', new_node: 'ListNode') -> None:
        """
        insert new node after a node
        node = node in the list
        new_node = new node to insert
        """
        new_node = self.make_node(new_node)
        new_node.next = node.next
        node.next = new_node

    def delete_after(self, node: 'ListNode') -> None:
        """
        delete the node past this one
        assume node is not a tail
        """
        node.next = node.next.next
