from binary_search_tree import BinarySearchTree

BST = BinarySearchTree()

BST.insert(6)
BST.insert(16)
BST.insert(3)
BST.insert(2)
BST.insert(4)
BST.insert(5)
BST.insert(64)
BST.insert(160)

print(BST.pre_order())
print(BST.level_order())
