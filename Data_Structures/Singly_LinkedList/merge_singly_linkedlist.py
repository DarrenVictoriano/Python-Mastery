"""
This module merge two singly LinkedList.
This assume that the LinkedLists are sorted.
"""

from simple_singly_list import ListNode


def merge_two_sorted_list(L1: 'ListNode',
                          L2: 'ListNode') -> 'ListNode':

    # Creates place holder for the ListNodes
    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next

    # Appends the remaining node of L1 and L2
    tail.next = L1 or L2
    return dummy_head.next
