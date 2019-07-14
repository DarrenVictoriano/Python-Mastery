from singly_linkedlist import SinglyLinkedList

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
