"""
This module merge two singly LinkedList.
This assume that the LinkedLists are sorted.
"""

from singly_linkedlist import SinglyLinkedList


def merge_two_sorted_list(L1: SinglyLinkedList,
                          L2: SinglyLinkedList) -> SinglyLinkedList:

    # Creates place holder for the ListNodes
    dummy_head = tail = SinglyLinkedList()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next_node, L1 = L1, L1.next_node
        else:
            tail.next_node, L2 = L2, L2.next_node
        tail = tail.next_node

    # Append the remaining node of L1 or L2
    tail.next_node = L1 or L2
    return dummy_head.next_node
