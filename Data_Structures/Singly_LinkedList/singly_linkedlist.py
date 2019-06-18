"""
this module is an implementaion of the singly linkedlist
node class:
    self.val
    self.next

linkedlist class:
    self.head
"""


class Node():
    """ node class for singly-linkedlist """

    def __init__(self, data, next_node=None):
        self.val = data
        self.next = next_node

    def get_data(self):
        """ getter function for node value """
        return self.val

    def set_data(self, data):
        """ setter function for node value """
        self.val = data

    def get_next(self):
        """ getter for next node """
        return self.next

    def set_next(self, data):
        """ setter for the next node """
        self.next = data


class SinglyLinkedList():
    """ singly-linkedlist implemantation """

    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self):
        """ return size of the list """
        return self.size

    def print_all(self):
        """ print all data in the list """
        # define a variable to hold the head node
        cur_node = self.head

        # traverse linearly until the end node
        while cur_node:
            # print each data
            print(cur_node.val)
            # assign var to the next node
            cur_node = cur_node.get_next()

    def insert_node(self, data):
        """ this will insert new node as head, so O(1) time complexity """
        # make a new node using the data and
        # pass the current head as the next node
        new_node = Node(data, self.head)
        # make the head as the new node then increase the size by one
        self.head = new_node
        self.size += 1
        return True

    def find(self, data):
        """ returns true if element is found else returns false """
        curr_head = self.head

        while curr_head:
            if curr_head.get_data() == data:
                # if data is found return true
                return True
            # assign curr_head to the next node
            curr_head = curr_head.get_next()
        return False

    def remove(self, data):
        """ remove node from the list """
        prev_node = None
        curr_node = self.head

        while curr_node:
            # if we found the data, proceed to delete
            if curr_node.get_data() == data:
                if prev_node:
                    # set next node of prev to next node of curr
                    prev_node.set_next(curr_node.get_next())
                else:
                    # simply point the head to next node of curr
                    self.head = curr_node.get_next()
                self.size -= 1
                return True
            # if we haven't find the data yet
            # assigned the current to as the previous node
            prev_node = curr_node
            # assgined the current node to the next node
            curr_node = curr_node.get_next()
        # data is not found
        return False
