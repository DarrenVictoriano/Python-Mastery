# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: TreeNode) -> None:
    if not root:
        return

    inorder_traversal(root.left)
    print("do the base case here")
    inorder_traversal(root.right)
