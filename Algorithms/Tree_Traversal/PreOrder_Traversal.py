# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root: TreeNode) -> None:
    if not root:
        return

    print("Do the base case here")

    preorder_traversal(root.left)
    preorder_traversal(root.right)

