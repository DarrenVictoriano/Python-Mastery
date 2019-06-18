"""
My Own implementation of
Binary Search Tree
"""

from queue import Queue


class Node():
    """ Node class with no duplicates """

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert(self, data):
        """ add data to Node """

        if self.data == data:
            # so no duplicate nodes
            return False
        elif self.data > data:
            # if root node is larger than data
            # check if left child is empty
            if self.left_child:
                # if left_child is NOT empty
                # call the insert method of the left_child
                # then return it to run recursively
                return self.left_child.insert(data)
            else:
                # if left child is empty
                # add data as new node
                self.left_child = Node(data)
                return True
        else:
            # if root node is lesser than data
            # check if right child is empty
            if self.right_child:
                # if right_child is NOT empty
                # call the insert method of the right_child
                # then return it to run recursively
                return self.right_child.insert(data)
            else:
                # if right_child is empty
                # add data as new Node
                self.right_child = Node(data)
                return True

    def find(self, data):
        """ find node value """
        if self.data == data:
            # we found it
            return True
        elif self.data > data:
            # if node is greater then the data
            # look in the left_child
            if self.left_child:
                # if left_child is NOT empty
                # call left_child's find method recursively
                return self.left_child.find(data)
            else:
                # if left_child is empty, value not found
                return False
        else:
            # if node is lesser than the data
            # look in the right_child
            if self.right_child:
                # if right child is not empty
                # call the right_child's find method recursively
                return self.right_child.find(data)
            else:
                # data not found
                return False

    def pre_order(self):
        """ order the node using pre-order travesal """

        if self:
            # if there is an instance of of the class
            # print the root node
            print(str(self.data), end=" ")

            if self.left_child:
                # if there is a left child call preorder recursively
                self.left_child.pre_order()

            if self.right_child:
                # if there is a left child call preorder recursively
                self.right_child.pre_order()

    def post_order(self):
        """ order the node using post-order traversal """

        if self:
            # of there is an instance of the class
            # check left child first
            if self.left_child:
                # if there is a left child
                # call post order recursively
                self.left_child.post_order()
            if self.right_child:
                # if there is a right child
                # call post order recursively
                self.right_child.post_order()

            # then print the root node if no child
            print(str(self.data), end=" ")

    def in_order(self):
        """ order the nodes using in-order traversal """
        if self:
            # if there is an instance of the class
            if self.left_child:
                # check left child then call recursively this method
                self.left_child.in_order()

            # print the value
            print(str(self.data), end=" ")

            if self.right_child:
                # check right child then call this function recursively
                self.right_child.in_order()

    def level_order(self):
        """ order the nodes using level-order traversal  """
        if self:
            # if there is an instance of the class
            # create a Queue and pass in the root node
            queue = Queue()
            queue.enqueue(self)

            while len(queue) > 0:
                # while there is an item in the queue
                # print the nodes value via peek function of Queue
                print(str(queue.peek()), end=" ")
                # removed Queues next in line value and assign it to node
                node = queue.dequeue()

                # if node have child value add that to the queue
                if node.left_child:
                    queue.enqueue(node.left_child)
                if node.right_child:
                    queue.enqueue(node.right_child)

    def get_size(self):
        """ get size of nodes """
        if self.left_child and self.right_child:
            # cout the root as 1 + left and right child
            return 1 + self.left_child.get_size() + self.right_child.get_size()
        elif self.left_child:
            # if only left child have value
            return 1 + self.left_child.get_size()
        elif self.right_child:
            # if only right child have value
            return 1 + self.right_child.get_size()
        else:
            # if no more child
            return 1

    def get_height(self):
        """ get the height level of the tree """
        if self.left_child and self.right_child:
            return 1 + max(self.left_child.get_height(), self.right_child.get_height())
        elif self.left_child:
            return 1 + self.left_child.get_height()
        elif self.right_child:
            return 1 + self.right_child.get_height()
        else:
            return 1  # 0 if you dont want to count root
