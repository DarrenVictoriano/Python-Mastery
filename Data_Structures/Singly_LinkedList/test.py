from singly_linkedlist import SinglyLinkedList
import merge_singly_linkedlist as MSL
from simple_singly_list import ListNode

lst = SinglyLinkedList()
for i in range(0, 10):
    lst.insert(i)

print("all")
lst.print_all()
print(f'current size is: {lst.get_size()}')
lst.remove(4)
print("removed 4")
lst.print_all()
print(f'current size is: {lst.get_size()}')

L1 = ListNode()
for i in range(0, 10, 2):
    L1.insert(i)

L2 = ListNode()
for i in range(4, 30, 3):
    L2.insert(i)

print(MSL.merge_two_sorted_list(L1, L2))
