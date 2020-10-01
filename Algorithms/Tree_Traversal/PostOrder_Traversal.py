# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorder_traversal(root: TreeNode) -> None:
    if not root:
        return

    postorder_traversal(root.left)
    postorder_traversal(root.right)

    print("Do the base case here")
